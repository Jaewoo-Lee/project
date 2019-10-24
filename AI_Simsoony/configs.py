# -*- coding: utf-8 -*-
import tensorflow as tf

# tf.app.flags.DEFINE_string('f', '', 'kernel') #
# tf.app.flags.DEFINE_integer('layer_size', 3, 'layer size') # 멀티 레이어 크기 (multi rnn)
# tf.app.flags.DEFINE_string('data_path', './data_in/ChatBotData.csv', 'data path') #  데이터 위치
# tf.app.flags.DEFINE_integer('embedding_size', 128, 'embedding size') # 임베딩 크기
# tf.app.flags.DEFINE_boolean('embedding', True, 'Use Embedding flag') # 임베딩 유무 설정
# tf.app.flags.DEFINE_boolean('multilayer', True, 'Use Multi RNN Cell') # 멀티 RNN 유무

# tf.app.flags.DEFINE_integer('batch_size', 64, 'batch size')  # 배치 크기
# tf.app.flags.DEFINE_integer('train_steps', 20000, 'train steps')  # 학습 에포크
# tf.app.flags.DEFINE_float('dropout_width', 0.5, 'dropout width')  # 드롭아웃 크기
# tf.app.flags.DEFINE_integer('embedding_size', 128, 'embedding size')  # 가중치 크기
# tf.app.flags.DEFINE_float('learning_rate', 1e-3, 'learning rate')  # 학습률
# tf.app.flags.DEFINE_integer('shuffle_seek', 1000, 'shuffle random seek')  # 셔플 시드값
# tf.app.flags.DEFINE_integer('max_sequence_length', 25, 'max sequence length')  # 시퀀스 길이
# tf.app.flags.DEFINE_integer('model_hidden_size', 128, 'model weights size')  # 모델 가중치 크기
# tf.app.flags.DEFINE_integer('ffn_hidden_size', 512, 'ffn weights size')  # ffn 가중치 크기
# tf.app.flags.DEFINE_integer('ff_input', 2, 'ff input size')  # ff label 크기
# tf.app.flags.DEFINE_integer('attention_head_size', 4, 'attn head size')  # 멀티 헤드 크기
# tf.app.flags.DEFINE_integer('layer_size', 2, 'layer size')  # 학습 속도 및 성능 튜닝
# tf.app.flags.DEFINE_string('data_path', 'C:/ssafygit3/ai-sub1/sub3/data_in/ChatBotData.csv', 'data path')  # 데이터 위치
# tf.app.flags.DEFINE_string('vocabulary_path', 'C:/ssafygit3/ai-sub1/sub3/data_out/vocabularyData.voc', 'vocabulary path')  # 사전 위치
# tf.app.flags.DEFINE_string('check_point_path', 'C:/ssafygit3/ai-sub1/sub3/data_out/check_point', 'check point path')  # 체크 포인트 위치
# tf.app.flags.DEFINE_boolean('xavier_initializer', True, 'set xavier initializer')  # 형태소에 따른 토크나이징 사용 유무
# tf.app.flags.DEFINE_boolean('serving', False, 'Use Serving') #  서빙 기능 지원 여부
# tf.app.flags.DEFINE_boolean('tokenize_as_morph', False, 'set morph tokenize') # 형태소에 따른 토크나이징 사용 유무

tf.app.flags.DEFINE_integer('batch_size', 64, 'batch size') # 배치 크기
# tf.app.flags.DEFINE_integer('train_steps', 50000, 'train steps') # 학습 에포크
# tf.app.flags.DEFINE_float('dropout_width', 0.1, 'dropout width') # 드롭아웃 크기
# tf.app.flags.DEFINE_integer('layer_size', 1, 'layer size') # 멀티 레이어 크기 (multi rnn)
# tf.app.flags.DEFINE_integer('hidden_size', 128 , 'weights size') # 가중치 크기
# tf.app.flags.DEFINE_float('learning_rate', 1e-4, 'learning rate') # 학습률
# tf.app.flags.DEFINE_float('teacher_forcing_rate', 0.7, 'teacher forcing rate') # 학습시 디코더 인풋 정답 지원율
tf.app.flags.DEFINE_string('data_path', 'C:/ssafygit3/ai-sub1/sub3/data_in/ChatBotData.csv', 'data path')  # 데이터 위치
tf.app.flags.DEFINE_string('vocabulary_path', 'C:/ssafygit3/ai-sub1/sub3/data_out/vocabularyData.voc', 'vocabulary path')  # 사전 위치
# tf.app.flags.DEFINE_string('check_point_path', 'C:/ssafygit3/ai-sub1/sub3/data_out/check_point', 'check point path')  # 체크 포인트 위치
# tf.app.flags.DEFINE_string('check_point_path2', 'C:/ssafygit3/ai-sub1/sub3/data_out2/check_point', 'check point path2')  # 체크 포인트 위치
# tf.app.flags.DEFINE_string('save_model_path', 'C:/ssafygit3/ai-sub1/sub3/data_out2/model', 'save model') # 모델 저장 경로
# tf.app.flags.DEFINE_integer('shuffle_seek', 1000, 'shuffle random seek') # 셔플 시드값
tf.app.flags.DEFINE_integer('max_sequence_length', 25, 'max sequence length') # 시퀀스 길이
# tf.app.flags.DEFINE_integer('embedding_size', 128, 'embedding size') # 임베딩 크기
# tf.app.flags.DEFINE_boolean('embedding', True, 'Use Embedding flag') # 임베딩 유무 설정
# tf.app.flags.DEFINE_boolean('multilayer', True, 'Use Multi RNN Cell') # 멀티 RNN 유무
# tf.app.flags.DEFINE_boolean('attention', True, 'Use Attention') #  어텐션 사용 유무
# tf.app.flags.DEFINE_boolean('teacher_forcing', True, 'Use Teacher Forcing') # 학습시 디코더 인풋 정답 지원 유무
# tf.app.flags.DEFINE_boolean('tokenize_as_morph', False, 'set morph tokenize') # 형태소에 따른 토크나이징 사용 유무
tf.app.flags.DEFINE_boolean('serving', False, 'Use Serving') #  서빙 기능 지원 여부
# tf.app.flags.DEFINE_boolean('loss_mask', False, 'Use loss mask') # PAD에 대한 마스크를 통한 loss를 제한

# Define FLAGS
DEFINES = tf.app.flags.FLAGS
