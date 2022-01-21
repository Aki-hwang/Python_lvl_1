import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
import os #이미지 저장할 폴더 만들기

if not os.path.exists("./네이버이미지"):    #있으면 false 반환 폴더가 있으면 폴스를 반환  즉 없으면 조건문에 들어가
    os.mkdir("./네이버이미지")

keyword = input("키워드입력 >>")

if not os.path.exists("./네이버이미지/{}".format(keyword)):  # #키워드 폴더 만들기
    os.mkdir("./네이버이미지/{}".format(keyword))

encoded = par.quote(keyword) #한글 url주소에 들어갈수 있는 특수한 문자열로 변경
url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(encoded)
code = req.urlopen(url)
soup = BeautifulSoup(code, "lxml")
image = soup.select("img")
cnt = 1
for i in image:
    img_url = i.attrs["src"]
    try:
        req.urlretrieve(img_url,"./네이버이미지/{}/{}.png".format(keyword,image.index(i)+1)) #두번째인자에 폴더를 만들꺼야
    except:
        print("이미지가 존재하지 않음")
    print("{} 이미지 크롤링 완료 {}".format(keyword, image.index(i)+1))


