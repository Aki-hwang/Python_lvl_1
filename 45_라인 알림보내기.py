import requests

api_key = "sgpEGSDzCvSyUUs8KhSE9QjQAvnAZfp7V6frQkBoqlV"
h = {"Authorization": "Bearer {}".format(api_key)} #빈칸과 괄호 주의하자
d = {"message" : "안녕 멍충이 컴퓨터로 하는거야."}

requests.post("https://notify-api.line.me/api/notify", headers=h,data=d)
