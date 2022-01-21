import requests
from bs4 import BeautifulSoup
sess = requests.session() #연결고리를 만들어준다 세션만들기

data = {"idsave_value": "",
"errorChk": "",
"gourl": "https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19930112%26mode%3D19930112%252F0002553622%252F1",
"bid": "talingpython",
"bpw": "xkfdldvkdlTjs2"
}
h= {"Referer": "https://secure.donga.com/membership/login.php?gourl=https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19930112%26mode%3D19930112%252F0002553622%252F1"}
sess.post("https://secure.donga.com/membership/trans_exe.php",headers=h, data=data) #포스트 요청
#세션으로 연결고리를 만들었기대문에 urlopen 필요 없어

#urlopen과 동일한 역활
code = sess.get("https://www.donga.com/archive/newslibrary/view?ymd=19930112&mode=19930112%2F0002553622%2F1")
soup = BeautifulSoup(code.text, "lxml") #get 사용시 .text 사용해라
title = soup.select("ul.news_list a")

for i in title:
    print(i.string)
    content_num = i.attrs["onclick"].replace("javascript:getNewsArticle('19930112/","").replace("1'); return false;","")
    content_url = "https://www.donga.com/archive/newslibrary/view?idx=19930112%2F{}%2F1".format(content_num)
    code = sess.get(content_url)
    soup = BeautifulSoup(code.text, "lxml")
    content = soup.select_one("div.article_txt")
    print(content.text.strip())
    print()






