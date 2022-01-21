# import urllib.request as req
# from bs4 import BeautifulSoup
#
# code = req.urlopen("http://www.cgv.co.kr/movies/?lt=1&ft=0") #서버가 코드를 주는 걸 확인 할 수 있어
# # print(code.read()) #read를 써야 읽을 수 있어
# #html 코드 이쁘게 정리하기
#
# soup = BeautifulSoup(code, "lxml") #예쁘게 정리 하는 과정
# # print(soup)
# # title = soup.select_one("strong.title") #태그명을 잡아 , 점은 속성 title은 속성값
# # print(title.string) #. string 요소의 내용만 빼욤
# #태그명이 div 속성명이 id 속성값이 movie인 요소 가져와
# # soup.select_one("div#movie")
# # 자손을 > 이렇게 표현해
# #div.box-contents strong.title   :공백기호 후손 표현
# # "." : class 속성
# # "#" : id 속성
# # ">" : 부모 자손 관계
# # " " : 조부모 자손 관계
# title = soup.select("div.sect-movie-chart strong.title")
# for i in title:
#     print(i.string)

import urllib.request as req
from bs4 import BeautifulSoup
code = req.urlopen("http://www.cgv.co.kr/movies/?lt=1&ft=0")
soup = BeautifulSoup(code, "lxml")
title = soup.select("div.sect-movie-chart strong.title")
for i in title:
    print(i.string)