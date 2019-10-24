#-*- coding: utf-8 -*-
from konlpy.tag import Okt
import pandas as pd
import tensorflow as tf
import enum
import os
import re
from sklearn.model_selection import train_test_split
import numpy as np
from configs import DEFINES
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.models import load_model

from tqdm import tqdm

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8', line_buffering=True)
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

PAD_MASK = 0
NON_PAD_MASK = 1

FILTERS = "([~.,!?\"':;)(])"
PAD = "<PAD>"
STD = "<SOS>"
END = "<END>"
UNK = "<UNK>"

PAD_INDEX = 0
STD_INDEX = 1
END_INDEX = 2
UNK_INDEX = 3

MARKER = [PAD, STD, END, UNK]
CHANGE_FILTER = re.compile(FILTERS)

train_model = load_model('C:/ssafygit3/ai-sub1/sub3/lstm_model.h5')

def load_data():
    data_df = pd.read_csv('C:/ssafygit3/ai-sub1/sub3/data_in/ChatBotData.csv', header=0)
    question, answer = list(data_df['Q']), list(data_df['A'])
    train_q, test_q, train_a, test_a = train_test_split(question, answer, test_size=0.01, random_state=39)
    return train_q, train_a, test_q, test_a

def prepro_noise_canceling(data):
    morph_analyzer = Okt()
    result_data = list()
    for sentence in tqdm(data):
        morphlized_seq = " ".join(morph_analyzer.morphs(sentence))
        result_data.append(re.sub(CHANGE_FILTER,"", morphlized_seq))
    return result_data

def tokenizing_data(data):
    words = []
    for sentence in data:
        sentence = re.sub(CHANGE_FILTER, "", sentence)
        for word in sentence.split():
            words.append(word)
    return [word for word in words if word]

def enc_processing(value, dictionary):

    seq_input_index = []
    seq_len = []
    value = prepro_noise_canceling(value)

    for seq in value:

        seq = re.sub(CHANGE_FILTER, "", seq)
        seq_index =[]

        for word in seq.split():
            if dictionary.get(word) is not None:
                seq_index.extend([dictionary[word]])
            else:
                seq_index.extend([dictionary[UNK]])

        if len(seq_index) > DEFINES.max_sequence_length:
            seq_index = seq_index[:DEFINES.max_sequence_length]

        seq_len.append(len(seq_index))

        seq_index += (DEFINES.max_sequence_length - len(seq_index)) * [dictionary[PAD]]
        seq_index.reverse()
        seq_input_index.append(seq_index)
    return np.asarray(seq_input_index), seq_len

def dec_output_processing(value, dictionary):

    seq_output_index = []
    seq_len = []
    value = prepro_noise_canceling(value)
    for seq in value:
        seq = re.sub(CHANGE_FILTER, "", seq)
        seq_index =[]
        seq_index.extend([dictionary[STD]])
        for word in seq.split():
            if dictionary.get(word) is not None:
                seq_index.extend([dictionary[word]])
            else:
                seq_index.extend([dictionary[UNK]])
        if len(seq_index) > DEFINES.max_sequence_length:
            seq_index = seq_index[:DEFINES.max_sequence_length]
        seq_len.append([PAD_MASK if num > len(seq_index) else NON_PAD_MASK for num in range (DEFINES.max_sequence_length)])
        seq_index += (DEFINES.max_sequence_length - len(seq_index)) * [dictionary[PAD]]
        seq_output_index.append(seq_index)

    return np.asarray(seq_output_index), np.asarray(seq_len)

def dec_target_processing(value, dictionary):

    seq_target_index = []
    seq_len = []
    value = prepro_noise_canceling(value)
    for seq in value:
        seq = re.sub(CHANGE_FILTER, "", seq)
        seq_index =[dictionary[word] for word in seq.split()]
        if len(seq_index) >= DEFINES.max_sequence_length:
            seq_index = seq_index[:DEFINES.max_sequence_length-1] + [dictionary[END]]
        else:
            seq_index += [dictionary[END]]
        seq_len.append([PAD_MASK if num > len(seq_index) else NON_PAD_MASK for num in range (DEFINES.max_sequence_length)])
        seq_index += (DEFINES.max_sequence_length - len(seq_index)) * [dictionary[PAD]]
        seq_target_index.append(seq_index)

    return np.asarray(seq_target_index), np.asarray(seq_len)

def rearrange(input, target):
    features = {"input": input}
    return features, target

def in_out_dict(input, length, target):
    features = {"input": input, "length": length}
    return features, target

def train_input_fn(train_input_enc, train_output_dec_len, train_target_dec, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((train_input_enc, train_output_dec_len, train_target_dec))
    dataset = dataset.shuffle(buffer_size=len(train_input_enc))
    assert batch_size is not None, "train batchSize must not be None"
    dataset = dataset.batch(batch_size, drop_remainder=True)
    dataset = dataset.map(in_out_dict)
    dataset = dataset.repeat()
    iterator = dataset.make_one_shot_iterator()
    return iterator.get_next()

def eval_input_fn(eval_input_enc, eval_target_dec, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((eval_input_enc, eval_target_dec))
    dataset = dataset.shuffle(buffer_size=len(eval_input_enc))
    assert batch_size is not None, "eval batchSize must not be None"
    dataset = dataset.batch(batch_size, drop_remainder=True)
    dataset = dataset.map(rearrange)
    dataset = dataset.repeat(1)
    iterator = dataset.make_one_shot_iterator()
    return iterator.get_next()

def load_voc():
    voc_list = []
    if (not (os.path.exists(DEFINES.vocabulary_path))):
        data_df = pd.read_csv(DEFINES.data_path, encoding='utf-8')
        question, answer = list(data_df['Q']), list(data_df['A'])
        question = prepro_noise_canceling(question)
        answer = prepro_noise_canceling(answer)

        datas = []
        datas.extend(question)
        datas.extend(answer)

        words = tokenizing_data(data)
        words = list(set(words))

        words[:0] = MARKER

        with open(DEFINES.vocabulary_path, 'w', encoding='utf-8') as voc_file:
            for word in words:
                voc_file.write(word + '\n')
    with open(DEFINES.vocabulary_path, 'r', encoding='utf-8') as voc_file:
        for line in voc_file:
            voc_list.append(line.strip())

    char2idx, idx2char = make_voc(voc_list)

    return char2idx, idx2char, len(char2idx)
def make_voc(voc_list):
    char2idx = {char: idx for idx, char in enumerate(voc_list)}
    idx2char = {idx: char for idx, char in enumerate(voc_list)}
    return char2idx, idx2char

def pred_next_string(value, dictionary):
    sentence_string = []
    if DEFINES.serving == True:
        for v in value['output']:
            sentence_string = [dictionary[index] for index in v]
    else:
        for v in value:
            sentence_string = [dictionary[index] for index in v['indexs']]

    print(sentence_string)
    answer = ""
    for word in sentence_string:
        if word not in PAD and word not in END:
            answer += word
            answer += " "
    print(answer)
    return answer
def convert_index_to_text(indexs, vocabulary):

    sentence = ''

    for index in indexs:
        if index == 2:
            break;
        if vocabulary.get(index) is not None:
            sentence += vocabulary[index]
        else:
            sentence.extend([vocabulary[UNK_INDEX]])
        sentence += ' '

    return sentence

def generate_text(input_seq):

    # train_model = load_model('C:/ssafygit3/ai-sub1/sub3/lstm_model.h5')
    char2idx, idx2char, voc_length = load_voc()
    check_input_enc = input_seq
    check_input_dec, check_input_dec_length = dec_output_processing([""], char2idx)
    input_encoder = check_input_enc[0].reshape(1, check_input_enc[0].shape[0])
    input_decoder = check_input_dec[0].reshape(1, check_input_dec[0].shape[0])
    results = train_model.predict([input_encoder, input_decoder])
    indexs = np.argmax(results[0], 1)
    print()
    print(indexs)

    sentence = convert_index_to_text(indexs, idx2char)
    print(sentence)
    inp = ""
    for value in sentence.split(" "):
        if value != "<PAD>":
            inp += value
        else :
            break
        inp += " "
    # print(inp)
    temp = 1
    while temp:
        check_input_dec, check_input_dec_length = dec_output_processing([inp], char2idx)
        input_decoder = check_input_dec[0].reshape(1, check_input_dec[0].shape[0])
        results = train_model.predict([input_encoder, input_decoder])
        indexs = np.argmax(results[0], 1)
        sentence = convert_index_to_text(indexs, idx2char)
        inp = ""
        for value in sentence.split(" "):
            if value != "<PAD>":
                inp += value
            else :
                break
            inp += " "

        print()
        print(indexs)
        print(sentence)
        for index in indexs:
            if index == 0 :
                break
            if index == 2 :
                temp = 0
                break
    return sentence

def main(self):
    char2idx, idx2char, voc_length = load_voc()

if __name__ == '__main__':
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)
    tf.compat.v1.app.run(main)
