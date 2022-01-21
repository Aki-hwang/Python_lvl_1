from selenium import webdriver
import time


option = webdriver.ChromeOptions()
option.add_argument("headless")  #브라우저 창이 안뜨기때문에 좀더 빠르게 할수 있다.
browser = webdriver.Chrome(options=option)
# browser = webdriver.Chrome("./chromdriver")

#다음 로그인 사이트로 이동
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net")
id = browser.find_element_by_css_selector("input#id")
id.send_keys("talingpython") #키를 넣게 만들어
pwd = browser.find_element_by_css_selector("input#inputPwd")
pwd.send_keys("q1w2e3!@#")
button = browser.find_element_by_css_selector("button#loginBtn").click() #클릭동작
time.sleep(3)
browser.get("https://mail.daum.net/") #이메일 함으로 이동
time.sleep(2)
title = browser.find_elements_by_css_selector("strong.tit_subject")
for i in title:
    print(i.text) #뷰티풀 숩은 .string /셀레니움은 .text
browser.close()
#셀레니움 단점
#1. 일단 너무 느리다 뷰티풀 숩의 10배 정도
#2. time 시간을 잡기 힘들다
#셀레니움을 꼭 써야만 하는 상황
#1. 로그인이 필요한 사이트
#2. 웹페이지가 동적일때