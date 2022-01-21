import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
from konlpy.tag import Okt
from collections import Counter #단어수 세기
import wordcloud #단어구름을 위해
import matplotlib.pyplot as plt #단어 구름을 새창으로 띄우기 위해
from PIL import Image #단어구름 모양 설정을 위해
import numpy as np #단어구름 모양 설정을 위해


keyword ="코딩"
encoded = par.quote(keyword)
output_total = ""
code = req.urlopen("https://www.joongang.co.kr/search/news?keyword={}".format(encoded))
soup = BeautifulSoup(code, "lxml")
news = soup.select("h2.headline a")
for i in news:
    print("제목 :",i.text)
    print("링크 :",i.attrs["href"])
    code_news = req.urlopen(i.attrs["href"])
    soup_news = BeautifulSoup(code_news, "lxml")
    content = soup_news.select_one("div#article_body")
    # print(content.text.strip().replace("  ","")) #strip()  양쪽의 쓸데 없는 공백을 제거해준다
    result = content.text.strip().replace("  ","") #strip()  양쪽의 쓸데 없는 공백을 제거해준다
    output_total += result
    # print(result)

# #형태소 분석하는
okt = Okt()
nons_list = okt.nouns(output_total)
# print(nons_list)
#한글자짜리 불용어 제거
for non in nons_list:
    if len(non) == 1:
        nons_list.remove(non)
# print(nons_list)
cnt = Counter(nons_list)
print(cnt)

#이미지 불러오기
image_list = np.array(Image.open("./down_image.jpg"))
image_color = wordcloud.ImageColorGenerator(image_list)


#단어구름 만들기
cloud_image = wordcloud.WordCloud(font_path="./NanumMyeongjoBold.ttf", background_color="white", mask=image_list).generate_from_frequencies(cnt)
#단어구름 이미지 띄우기
plt.figure(figsize=(10,10))
plt.imshow(cloud_image.recolor(color_func=image_color), interpolation="bilinear")
plt.axis("off")
plt.show()



