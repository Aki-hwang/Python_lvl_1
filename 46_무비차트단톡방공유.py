import urllib.request as req
import requests
from bs4 import BeautifulSoup
api_key = "sgpEGSDzCvSyUUs8KhSE9QjQAvnAZfp7V6frQkBoqlV"
h = {"Authorization": "Bearer {}".format(api_key)}  # 빈칸과 괄호 주의하자
code = req.urlopen("http://www.cgv.co.kr/movies/?lt=1&ft=0")
soup = BeautifulSoup(code, "lxml")
title = soup.select("div.sect-movie-chart strong.title")
image = soup.select("span.thumb-image > img")

for i in range(len(title)):
    d = {"message": "{}위 : {}".format(i+1, title[i].string),
    "imageThumbnail" : image[i].attrs["src"],
    "imageFullsize" : image[i].attrs["src"]}
    requests.post("https://notify-api.line.me/api/notify", headers=h, data=d)
    if i > 8:
        break








