import requests
import json
import folium #map 위해
import os #자동실행하기 위해
from selenium import webdriver

api_key = "644241457768657239355869517262"
url = "http://openapi.seoul.go.kr:8088/{}/json/bikeList/1/10/".format(api_key)
data = requests.get(url)
result = json.loads(data.text) #json을 딕셔너리 자료형으로 변환
# print(json.dumps(result, indent="\t")) #json을 dumps가 예쁘게 정렬해죠
# print(result["rentBikeStatus"]["row"]) #리스트 자료형을 쓸때는 반드시 for으로 잡아줘야해
comp = result["rentBikeStatus"]["row"]
print(json.dumps(result, indent="\t"))