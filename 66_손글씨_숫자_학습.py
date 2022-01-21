from sklearn.svm import SVC
import pandas as pd
from sklearn.metrics import accuracy_score
import pickle

train = pd.read_csv("./mnist/train.csv")
valid = pd.read_csv("./mnist/t10k.csv")

train_label = train.iloc[:, 0] #모든행에 1번쨰 열
train_data = train.iloc[:, 1:] #모든 행에 2번째 ㅇ열부터 끝까지

valid_label = train.iloc[:, 0] #모든행에 1번쨰 열
valid_data = train.iloc[:, 1:] #모든 행에 2번째 ㅇ열부터 끝까지

model = SVC()
model.fit(train_data, train_label)
result = model.predict(valid_data)
score = accuracy_score(result, valid_label)

print(score)
#모델을 파일 형태로 저장하기 위해
f = open("./mnist_model.pkl", "wb")
pickle.dump(model, f)
f.close()