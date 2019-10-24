# 심순이

## Language
> python


## 프로젝트 개요
![개요](https://user-images.githubusercontent.com/13237010/67460740-b8e37900-f676-11e9-9501-2390a7097a4f.PNG)
자연어 처리에서 Tokenizing 방식으로 Okt의 morph함수를 사용하였다.
단어를 문법적으로 쪼개 주면서, 단어의 형태를 유지하는 함수이기 때문.
``` 
ex) 그럴 거에요 -> 그러 + ㄹ + 거 + 에요   ( X )
    그럴 거에요 -> 그럴 + 거 + 에요   ( ㅇ ) 
```


## 사용한 모델
![seq2seq설명](https://user-images.githubusercontent.com/13237010/67460775-cdc00c80-f676-11e9-8be7-83d8c1d25172.PNG)
시퀀스 투 시퀀스 모델은 챗봇, 번역기에 많이 사용되는 모델 
Encoder와 Decoder, 두 개의 아키텍처로 구성되어 있고, Encoder에서 생성된 단어의 정보(Context Vector)를 기반으로 Decoder가 단어를 하나씩 출력되는 방식으로 동작한다

RNN의 경우. 말그대로 순환의 구조를 가지는 모델
n항의 출력이 input에 포함되어 n+1항의 출력에 영향을 끼치는 구조


## seq2seq 모델의 문제점
![seq2seq문제점](https://user-images.githubusercontent.com/13237010/67460803-ddd7ec00-f676-11e9-91ba-fb356528ffc2.PNG)
RNN의 구조의 특징에서 발생하는 문제점
단어의 수가 많은 문장일수록 앞 쪽에 위치한 단어가 뒤 쪽 단어에 대한 영향이 급격하게 낮아진다.
이는 챗봇의 문맥 파악 여부에 치명적인 영향을 미쳐 대답으로 비문이 출력되는 등의 완성도 저하문제를 발생시킨다.
또한, 문장 요소의 순서 변경이나 어미 변화 같은 이유로 input 데이터 셋에 포함되어 있지 않은 문장을 input으로 입력시켰을 시,
문맥에 따른 대답이 아닌 엉뚱한 대답이 나오는 문제가 발생한다.


## 문제점 보완 알고리즘
![LSTM](https://user-images.githubusercontent.com/13237010/67460836-f6e09d00-f676-11e9-876e-bf47054c82db.PNG)
LSTM과 Attention function 중 LSTM 기법을 사용하여 이같은 문제를 보완하였다.

forget gate에서 각각의 단어를 계속 가지고 갈 것인지, 버릴(forget) 것인지 판단하여 결과적으로 문장을 이루는 단어의 수를 추리는 효과가 있다.

방법으로는, ht-1과 Xt에 sigmoid를 취해 나오는 결과값(0 또는 1)에 따라 forget gate에서 버릴 지, 취할 지 여부를 판단한다.
이를 도식화 하면 아래와 같다.

![LSTM도식](https://user-images.githubusercontent.com/13237010/67460866-0fe94e00-f677-11e9-9606-d48777d7ae79.png)


## 챗봇 학습 방식
![학습방식](https://user-images.githubusercontent.com/13237010/67460891-1f689700-f677-11e9-9b02-34d952bc8793.PNG)
인코더 입력, 디코더 입력, 디코더 출력 총 3개의 데이터셋을 사용한다.
인코더 입력에는 질문으로 사용하는 문장, 
디코더 입력은 문장의 시작을 의미하는 <START> 태그로 시작하는 답변 문장,
디코더 출력은 문장의 끝을 의미하는 <END> 태그로 끝나는 답변 문장이 각각 들어있다.


## 챗봇이 답변을 추론하는 방식
![추론과정](https://user-images.githubusercontent.com/13237010/67460915-2db6b300-f677-11e9-8ff0-5d000053c3de.PNG)
입력 문장이 입력되면 문장 전체와 <START> 태그에서 [밥]을 출력한다.
입력 문장과 '밥'에서 [먹어]를,
입력 문장과 '먹어'에서 <END>를 출력하여 결과적으로 [밥 먹어]라는 문장을 완성하게 된다.


## 동작 화면
![동작화면](https://user-images.githubusercontent.com/13237010/67460916-2e4f4980-f677-11e9-8f5b-63db9e0c6e94.PNG)
문법적으로 오류가 없는 문장이 출력되는 모습을 볼 수 있다.
'지갑을 잃어버렸어'는 입력 데이터 셋에 포함되지 않는 input임에도 불구하고 의미에 적합한 답변을 출력하는 것을 볼 수 있다.
