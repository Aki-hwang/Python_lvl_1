import urllib.request as req
from bs4 import BeautifulSoup
f = open("알라딘중고샵.txt", "w")

page_num = 1
while True:
    url = "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&KeyWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyLastWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&ViewRowCount=25&page={}".format(page_num)
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "lxml")
    title = soup.select("a.bo3 > b")
    price = soup.select("a.bo_used > b") #2개를 포문 하고 싶을떄
    # for i in title:
    #     print(i.string)
    if len(title) == 0: #마지막 페이지
        break
    for i in range(len(title)):
        print(title[i].string, price[i].string)
        f.write(title[i].string + "," + price[i].string + "\n")  #write 는 콤마 사용 불가
    page_num += 1
f.close()