from sklearn.svm import SVC
import  pandas as pd
from sklearn.model_selection import train_test_split #학습용과 검증용을 자동으로 나누어 주기 이ㅜ해 사용
from sklearn.metrics import accuracy_score #채점을 하기 위해 불러옴

#지도학습을 하는 코드 작성
#label 컴퓨터가 최종적으로 예측할 것 / data는 기본 내용
df = pd.read_csv("./머신러닝/iris.csv")
label = df["variety"]
data = df[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
#알아서 트레인과 벨리드를 나누어 준다
train_data, valid_data, train_label, valid_label = train_test_split(data, label)


#학습시키기
model = SVC() #이 알고리즘으로 할꺼애 support vector machine classifier /인공지능 모델을 불러와죠
model.fit(train_data, train_label) #학습 시작


#자동으로 시험문제 내볼까
result = model.predict(valid_data)

#채점하기
score = accuracy_score(result, valid_label)
# #이제 질문을 던져볼까
# result = model.predict([
#     [4.2, 1.2, 5.2, 2.3], [1.2,3.4,1.2,4.3], [3.1,4.3,5.1,3.6]
# ])
print(score) #검증결과 확인

