from selenium import webdriver
import time
import os
from twilio.rest import Client

browser = webdriver.Chrome("./chromedriver")
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
id = browser.find_element_by_css_selector("#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)
browser.get("http://cafe.daum.net/talingpython")
time.sleep(3)
# 가입인사 게시판 클릭
# No such element ... error -->
# 1. CSS 선택자 잘썼나 확인
# 2. time.sleep() 을 길게 조정
# 3. 프레임 안에 있는거 아닌가 즉 내부에 html이 또있거나 frame이 있는거 아닌가
browser.switch_to.frame(browser.find_element_by_css_selector("iframe#down")) # 프레임 전환
browser.find_element_by_css_selector("#fldlink_rRa6_347").click()
time.sleep(2)
#과거의 게시물 제목이 들어 있는 메모장 불러옴
try:
    f = open("./중고나라.txt", "r")
    ref = f.readlines()
except: #파일 새로 생성해야해
    f = open("./중고나라.txt", "w") #w 모드는 파일이 없으면 새로 만들거든
    ref = []

#게시물 제목 크롤링
title = browser.find_elements_by_css_selector("a.txt_item")
new_one = 0
for i in title:
    if not (i.text + "\n") in ref: #크롤링한 제목이 과거의 글이 아니라면
        f = open("./중고나라.txt", "a")
        f.write(i.text + "\n")
        if "스마트폰" in i.text: #관심있는 물건이라면
            new_one += 1
f.close()
# print("{} 관련 글이 {}개 올라왔습니다".format("스마트폰", new_one))
browser.close()
#https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1&newCustomer=true

if new_one >= 1:
    account_sid = "AC629cc3a3c56ffa4c1a9536187ded2739"
    auth_token = "359be9bcae0eefe3b519aa2a54bed998"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="{} 관련 글이 {}개 올라왔습니다. https://cafe.daum.net/talingpython/rRa6".format("스마트폰", new_one),
                         from_='+17373771136',
                         to='+821043670778'
                     )

