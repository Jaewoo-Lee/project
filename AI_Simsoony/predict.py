#-*- coding: utf-8 -*-
import tensorflow as tf
import data
import os
import sys
import model as ml
import pickle
from tensorflow.keras.models import load_model
import numpy as np

from configs import DEFINES

if __name__ == '__main__':
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
    arg_length = len(sys.argv)

    if (arg_length < 2):
        raise Exception("Don't call us. We'll call you")

    char2idx, idx2char, vocabulary_length = data.load_voc()
    input = ""
    for i in sys.argv[1:]:
        input += i
        input += " "
    print()
    print(input)

    train_model = load_model('C:/ssafygit3/ai-sub1/sub3/lstm_model.h5')
    check_input_enc, check_input_enc_length = data.enc_processing([input], char2idx)
    sentence = data.generate_text(check_input_enc)
    print()
    print("answer : ",sentence)
