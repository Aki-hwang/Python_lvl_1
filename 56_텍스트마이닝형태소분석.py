
#윈도우 경우pip install jpype1==1.2.0
# 형태소 분석을 위해 pip install konlpy
from konlpy.tag import Okt

okt = Okt()
result = okt.pos("안녕하세요 파이썬 공부중입니다")
print(result)

