from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

okt = Okt()
tokenizer = Tokenizer(19417, oov_token = 'OOV')
with open('wordIndex.json') as json_file:
  word_index = json.load(json_file)
  tokenizer.word_index = word_index
#텐서플로오 1에 가까울수록 긍정적 0에 가까우면 부정적이야
loaded_model: object = load_model('best_model.h5')
def sentiment_predict(new_sentence):
    print(new_sentence)
    max_len = 30
    stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
    new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
    new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
    encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
    pad_new = pad_sequences(encoded, maxlen = max_len) # 패딩
    score = float(loaded_model.predict(pad_new)) # 예측
    return score
#위쪽은 감성분석을 위한 준비
#===============================================================================================
#아래는 네이버 영화 리뷰를 가져옴
from bs4 import BeautifulSoup
import urllib.request as req

page_num = 1
previous_page_result = ""
while True:
    code = req.urlopen("https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=10106&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}".format(page_num))
    soup = BeautifulSoup(code, "html.parser")
    comment = soup.select("li > div.score_reple > p > span")
    if comment[-1].text.strip() == previous_page_result:
        break
    for i in comment:
        i = i.text.strip()
        if i == "관람객":
            continue
        # print(i)
        score = sentiment_predict(i) #숫자를 반환해죠 << 이것만 우리가 쓰는거야
        if score >= 0.5:
            print("{:.2f}% 확율로 긍정입니다".format(score*100)) # :.2f 하면 소수점 2개만 나와
        else:
            print("{:.2f}% 확율로 부정입니다".format(100-(score * 100)))
        print("------------------")
    previous_page_result = i
    page_num += 1