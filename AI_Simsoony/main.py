#-*- coding: utf-8 -*-

import tensorflow as tf
import model as ml
import data
import numpy as np
import pickle
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.models import load_model

from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
from rouge import Rouge

from configs import DEFINES

# Req. 1-5-1. bleu score 계산 함수
def bleu_compute():

    return None

# Req. 1-5-2. rouge score 계산 함수
def rouge_compute():

    return None

def main(self):
    char2idx, idx2char, vocabulary_length = data.load_voc()
    train_q, train_a, test_q, test_a = data.load_data()
    train_input_enc, train_input_enc_length = data.enc_processing(train_q, char2idx)
    train_target_dec, train_target_dec_length = data.dec_target_processing(train_a, char2idx)
    one_hot_data = np.zeros((len(train_target_dec), DEFINES.max_sequence_length, vocabulary_length))
    for i, sequence in enumerate(train_target_dec):
        for j, index in enumerate(sequence):
            one_hot_data[i, j, index] = 1
    y_decoder = one_hot_data
    train_input_dec, train_input_dec_length = data.dec_output_processing(train_a, char2idx)
    eval_input_enc, eval_input_enc_length = data.enc_processing(test_q, char2idx)
    eval_target_dec, _ = data.dec_target_processing(test_a, char2idx)

    train_model = load_model('C:/ssafygit3/ai-sub1/sub3/lstm_model.h5')
    # 에폭 반복
    check_input_enc, check_input_enc_length = data.enc_processing(["레시피대로 조리한 거 같은데 왜 맛이 없을까?"], char2idx)
    check_input_dec, check_input_dec_length = data.dec_output_processing(["손맛이 안 들어가서 그럴 수도 있어요"], char2idx)
    for epoch in range(4):
        print('Total Epoch :', epoch + 1)
        history = train_model.fit([train_input_enc, train_input_dec],
                            y_decoder,
                            epochs=5,
                            batch_size=DEFINES.batch_size,
                            verbose=1)
        # 정확도와 손실 출력
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print('accuracy :', history.history['acc'][-1])
        print('loss :', history.history['loss'][-1])
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        input_encoder = check_input_enc[0].reshape(1, check_input_enc[0].shape[0])
        input_decoder = check_input_dec[0].reshape(1, check_input_dec[0].shape[0])
        results = train_model.predict([input_encoder, input_decoder])
        indexs = np.argmax(results[0], 1)

        # 인덱스를 문장으로 변환
        sentence = data.convert_index_to_text(indexs, idx2char)
        print(sentence)
        print()
    train_model.save('C:/ssafygit3/ai-sub1/sub3/lstm_model.h5')

if __name__ == '__main__':
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)
    tf.compat.v1.app.run(main)

tf.logging.set_verbosity
