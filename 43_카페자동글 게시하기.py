from selenium import webdriver
import time

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
browser.find_element_by_css_selector("#fldlink_lF1R_309").click()
time.sleep(3)
# 글쓰기 버튼 클릭
browser.find_element_by_css_selector("#article-write-btn").click()
time.sleep(3)

# 제목 작성
subject = browser.find_element_by_css_selector(".title__input")
subject.send_keys("안녕하세요!!!!!!")
# 본문 작성
browser.switch_to.frame(browser.find_element_by_css_selector("#keditorContainer_ifr")) # 프레임 전환
content = browser.find_element_by_css_selector("#tinymce")
content.send_keys("너무나 반갑습니다.")
# # 발행 버튼 클릭
# #가장 밖의 프레임으로 전환 프레임 전환은 밖에서 안으로만 가능 즉 가장 밖으로 빠져나온다음에 다시 들어가야해
browser.switch_to.default_content() # 제일 바깥으로 빠져나옴.
browser.switch_to.frame(browser.find_element_by_css_selector("#down")) # 프레임 전환
browser.find_element_by_css_selector("button.btn_g.full_type1").click()
time.sleep(3)
browser.close()