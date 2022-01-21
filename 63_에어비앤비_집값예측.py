from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error #채점을 하기 위해 불러옴 회기모델 전용 체점 도구

df = pd.read_csv("./머신러닝/Airbnb.csv")
label = df["price"]
# data = df.iloc[1:5,3:6] #1행부터 4행까지, 3열부터 5열까지
data = df.iloc[:, 0:6] #모든 행 과 0열부터 5열
#알아서 트레인과 벨리드를 나누어 준다
train_data, valid_data, train_label, valid_label = train_test_split(data, label)

#학습시키기
model = LinearRegression()
model.fit(train_data, train_label)

#정확도 확인하기
result = model.predict(valid_data)
score = mean_squared_error(result, valid_label) ** (1/2) #루트를 해죠 ** 제곱 의미
# print(score) # 얼마나 정확한지 알수 확인하는 과정

#실제 우리집 집 범위를 넣으면 예상되는 가격을 알 수 있다.
my_house = model.predict([
    [0.000321, 0.43, 6.3, 4.1, 30, 50]
    ])
print(my_house)