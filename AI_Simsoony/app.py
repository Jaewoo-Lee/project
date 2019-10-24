import pickle
from threading import Thread
import sqlite3

import numpy as np
from flask import Flask
from slackclient import SlackClient
from slackeventsapi import SlackEventAdapter

import data
import model as ml
import tensorflow as tf
from tensorflow.keras.models import load_model
import re
from configs import DEFINES


# slack 연동 정보 입력 부분
SLACK_TOKEN = "xoxb-732087165399-731068897604-wL7BeYI2rJwZIDDGV7KdUVHQ"
SLACK_SIGNING_SECRET = "256655b417dd923fce838f6382b58040"

app = Flask(__name__)

slack_events_adaptor = SlackEventAdapter(SLACK_SIGNING_SECRET, "/listening", app)
slackclient = SlackClient(SLACK_TOKEN)

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
with open('C:/ssafygit3/ai-sub1/sub3/char2idx.csv','rb') as f:
    char2idx = pickle.load(f)
with open('C:/ssafygit3/ai-sub1/sub3/idx2char.csv','rb') as f:
    idx2char = pickle.load(f)
train_model = load_model('C:/ssafygit3/ai-sub1/sub3/lstm_model.h5')
# train_model = load_model('C:/ssafygit3/ai-sub1/sub3/lstm_model.h5')
# cnt = 0
FILTERS = "([~.,!?\"':;)(])"
CHANGE_FILTER = re.compile(FILTERS)
# Req. 2-2-1 대답 예측 함수 구현
def predict(input):

    print(input[12:])
    sentence = input[12:]
    check_input_enc, check_input_enc_length = data.enc_processing([input[12:]], char2idx)
    # seq_input_index = []
    # value = data.prepro_noise_canceling([input[12:]])
    #
    # for seq in value:
    #
    #     seq = re.sub(CHANGE_FILTER, "", seq)
    #     seq_index =[]
    #
    #     for word in seq.split():
    #         if char2idx.get(word) is not None:
    #             seq_index.extend([char2idx[word]])
    #         else:
    #             seq_index.extend([char2idx["<UNK>"]])
    #
    #     if len(seq_index) > DEFINES.max_sequence_length:
    #         seq_index = seq_index[:DEFINES.max_sequence_length]
    #
    #     seq_index += (DEFINES.max_sequence_length - len(seq_index)) * [char2idx["<PAD>"]]
    #     seq_index.reverse()
    #     seq_input_index.append(seq_index)
    # check_input_enc = np.asarray(seq_input_index)
    # # print(check_input_enc)
    # # print(check_input_enc_length)
    # # check_input_enc = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,5925,9590]]
    # # check_input_enc = np.asarray(check_input_enc)
    #
    sentence = data.generate_text(check_input_enc)
    # # train_model = load_model('C:/ssafygit3/ai-sub1/sub3/lstm_model.h5')
    # # check_input_enc = input_seq
    # check_input_dec, check_input_dec_length = data.dec_output_processing([""], char2idx)
    #
    # input_encoder = check_input_enc[0].reshape(1, check_input_enc[0].shape[0])
    # input_decoder = check_input_dec[0].reshape(1, check_input_dec[0].shape[0])
    # results = train_model.predict([input_encoder, input_decoder])
    # indexs = np.argmax(results[0], 1)
    # # print(indexs)
    #
    # sentence = data.convert_index_to_text(indexs, idx2char)
    # # print(sentence)
    # inp = ""
    # for value in sentence.split(" "):
    #     if value != "<PAD>":
    #         inp += value
    #     else :
    #         break
    #     inp += " "
    # # print(inp)
    # temp = 1
    # while temp:
    #     check_input_dec, check_input_dec_length = data.dec_output_processing([inp], char2idx)
    #
    #     input_decoder = check_input_dec[0].reshape(1, check_input_dec[0].shape[0])
    #     results = train_model.predict([input_encoder, input_decoder])
    #     indexs = np.argmax(results[0], 1)
    #     sentence = data.convert_index_to_text(indexs, idx2char)
    #     inp = ""
    #     for value in sentence.split(" "):
    #         if value != "<PAD>":
    #             inp += value
    #         else :
    #             break
    #         inp += " "
    #
    #     # print(sentence)
    #     for index in indexs:
    #         if index == 0 :
    #             break
    #         if index == 2 :
    #             temp = 0
    #             break
    return sentence

# Req 2-2-2. app.db 를 연동하여 웹에서 주고받는 데이터를 DB로 저장

# 챗봇이 멘션을 받았을 경우
@slack_events_adaptor.on("app_mention")
def app_mentioned(event_data):
    channel = event_data["event"]["channel"]
    text = event_data["event"]["text"]
    # print("체크")
    keywords = predict(text)
    slackclient.api_call('chat.postMessage',
        channel=channel,
        text=keywords
    )

@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"

if __name__ == '__main__':
    app.run()
