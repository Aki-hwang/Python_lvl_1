import urllib.request as req
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Chrome/66.0.3359.181'}
url = "https://scholar.google.com/scholar?start=0&q=((optical+device)+OR+(electrochemical+device)+OR+(electronic+device)+OR+(biosensor)+OR++(urine+sensor)+OR+(dipstick+test))+AND+((urinalysis)+OR+(molecular+diagnostic)+OR+(dipstick+test))+NOT+review&hl=ko&as_sdt=0,5&as_ylo=2022"
reqUrl = req.Request(url, headers=headers)
code = req.urlopen(reqUrl)
soup = BeautifulSoup(code, "lxml")
# wantPaper = soup.select("h3.gs_rt a")
wantPaper = soup.select("h3", {"class":"gs_rt"})
for i in wantPaper:
    print(i.text)