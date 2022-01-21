import openpyxl
from email.mime.text import MIMEText
import smtplib
#첨부 파일을 불러오기 위해
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#이메일 서비스를 파이썬에서 이용하기 위해
naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465) #보안연결 필요가 있어서 사용
naver_server.login("ysloveredeye", "Cjfwls98!@#")


book = openpyxl.load_workbook("./list (1).xlsx")
sheet = book.active
cnt = 0
for row in sheet.rows:
    if row[4].value == "X": #결제 안했다면
        continue
    data = row[0].value
    name = row[1].value
    your_mail = row[2].value
    product = row[3].value
    title = "{}님, XX 쇼핑몰입니다".format(name)
    content = """
안녕하세요 XX 쇼핑몰입니다
결제완료 안내 메일드립니다.
성함 : {}
날짜 : {}
상품 : {}""".format(name,data,product)
    email_content = MIMEMultipart()#택배와 편지를 모두 넣을 수 있는 거야
    email_content["From"] = "ysloveredeye@naver.com"
    email_content["To"] = your_mail
    email_content["Cc"] = "ysloveredeye@naver.com, ysloveredeye@naver.com"
    email_content["Subject"] = title
    msg = MIMEText(content, _charset="euc-kr")
    email_content.attach(msg)
    part = MIMEBase("application", "octet-stream") #택배박스에 어떤걸 넣는지 쓰는거야 즉 여기에는 파일이 들어가 있다.
    part.set_payload(open("./attachment_file (1).xlsx", "rb").read()) #rb 바이너리 형태로 보내겠다
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename=attachment_file (1).xlsx")
    email_content.attach(part)

    #메일만 보내는 경우
    # msg = MIMEText(content, _charset="euc-kr")#_charset="euc-kr" 한글쓰려고 넣어준거야
    # msg["From"] = "ysloveredeye@naver.com"
    # msg["To"] = your_mail
    # msg["Subject"] = title

# 그냥 센드매일 하면 이메일이 보내진다는거

    naver_server.sendmail("ysloveredeye@naver.com", your_mail, email_content.as_string())
    print("{}께 메일을 보냈습니다".format(name))
    cnt += 1
    if cnt % 20 == 0:
        naver_server.quit() #로그아웃을 하고
        naver_server.login("ysloveredeye", "Cjfwls98!@#")
        book = openpyxl.load_workbook("./list (1).xlsx")

