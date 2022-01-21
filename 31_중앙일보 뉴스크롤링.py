import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par

keyword = input("검색내용은 >> ")
encoded = par.quote(keyword)
code = req.urlopen("https://www.joongang.co.kr/search/news?keyword={}".format(encoded))
soup = BeautifulSoup(code, "lxml")
news = soup.select("h2.headline a")

for i in news:
    print("제목 :",i.text)
    print("링크 :",i.attrs["href"])
    code_news = req.urlopen(i.attrs["href"])
    soup_news = BeautifulSoup(code_news, "lxml")
    content = soup_news.select_one("div#article_body")
    print(content.text.strip().replace("  ","")) #strip()  양쪽의 쓸데 없는 공백을 제거해준다
#링플레이스를 사용해 2개 공백을 지워준다
