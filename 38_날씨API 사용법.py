import requests
import json

api_key = "626228b60e8abe78535d0b31445e9958"
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format("Seoul",api_key)
data = requests.get(url) #서버에 데이터 요청
result = json.loads(data.text) #Json 자료형을 딕셔너리로 바꿔줘
#aip는 CSV와 JSON 이중 하나의 형태로 우리에게 보내죠   JSON은 파이썬의 딕셔너리 자료형과 비슷하지만 파이썬은 다르게 파악한다
print("도시 : ",result["name"]) #딕셔너리 형태지만 단순하게 불러올수 없어 데이터 형식에 데해 알아봐야해
print("날씨 : ",result["weather"][0]["main"])#리스트 자료의 특징은 인덱스 번호로 값을 꺼내올수 있어

print("최저기온 : ",result["main"]["temp_min"])
print("최고기온 : ",result["main"]["temp_max"])

# temp_cont = result["main"]["temp_max"]
# temp_cont = (temp_cont-32)*5/9

