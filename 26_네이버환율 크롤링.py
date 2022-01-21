# import urllib.request as req
# from bs4 import BeautifulSoup
# code = req.urlopen("https://finance.naver.com/marketindex/")
# soup = BeautifulSoup(code, "lxml")
# money = soup.select("div.market1 span.value")
# # money = soup.select("span.value")
# # print(money)
# for i in money:  #리스트로 받기 때문에 for문을 사용해
#     print(i.string) # .sting은 Htm 요소인 경우만 쓸수 있어서 for문이 필요해
#

import urllib.request as req
from bs4 import BeautifulSoup
code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code, "lxml")
# money = soup.select("div.market1 span.value")
money = soup.select("span.value")
cnt = 0
for i in money:  #리스트로 받기 때문에 for문을 사용해
    print(i.string) # .sting은 Htm 요소인 경우만 쓸수 있어서 for문이 필요해
    cnt += 1
    if cnt == 4:
        break