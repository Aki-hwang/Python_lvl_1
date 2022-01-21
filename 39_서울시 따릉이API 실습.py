import requests
import json
import folium #map 위해
import os #자동실행하기 위해
from selenium import webdriver

api_key = "644241457768657239355869517262"
url = "http://openapi.seoul.go.kr:8088/{}/json/bikeList/1/500/".format(api_key)
data = requests.get(url)
result = json.loads(data.text) #json을 딕셔너리 자료형으로 변환
# print(json.dumps(result, indent="\t")) #json을 dumps가 예쁘게 정렬해죠
# print(result["rentBikeStatus"]["row"]) #리스트 자료형을 쓸때는 반드시 for으로 잡아줘야해
comp = result["rentBikeStatus"]["row"]
lat_sum = 0
lon_sum = 0
for i in comp: #마커의 중심을 잡기 위해 실행
    lat = float(i["stationLatitude"])
    lon = float(i["stationLongitude"])
    lat_sum += lat
    lon_sum += lon
lat_avr = lat_sum/len(comp)
lon_avr = lon_sum/len(comp)

map = folium.Map(location=[lat_avr,lon_avr], zoom_start=14)
for i in comp:
    bike_num = int(i["parkingBikeTotCnt"])
    station_name = i["stationName"]
    lat = i["stationLatitude"]
    lon = i["stationLongitude"]
    if bike_num < 3:
        color = "red"
    elif 3<= bike_num <7:
        color = "blue"
    elif 7<= bike_num:
        color = "green"

    folium.Marker(location=[lat, lon], popup=station_name, tooltip=bike_num, icon=folium.Icon(color=color)).add_to(map) #popup 마커 만들기,
    #tooltip 마우스 오버 했을때 바이크 갯수가나오게 해죠
map.save("./map.html")
file_path = os.path.abspath("./map.html")#파일의 절대 경로를 반환
browser = webdriver.Chrome('./chromedriver') #파일의 자동실행을 위해
browser.get(file_path) #윈도우 경우 가능
# browser.get("file://" + file_path) #맥사용자
# pip install selenium==3.12.0 #브라우저 창이 그냥 꺼질때

