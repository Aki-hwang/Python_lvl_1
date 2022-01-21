import urllib.request as req
from bs4 import BeautifulSoup

print("========메뉴========")
print("1. 미국")
print("2. 일본")
print("3. 유럽")
print("4. 중국")
print("==================")
menu = int(input("원하는 나라를 눌러라 >>>"))
unit = ["달라", "엔","유로","위안"]
money = int(input ("금액 입력 (단위 : {})".format(unit[menu-1])))
if menu ==2:
    money = money / 100
code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code, "lxml")
# money = soup.select("div.market1 span.value")
price = soup.select("span.value")
price = float(price[menu-1].string.replace(",", "")) #리플레이스 함수로 콤마를 모두 지워준다 / float로 변경 필요해
print(price * money)