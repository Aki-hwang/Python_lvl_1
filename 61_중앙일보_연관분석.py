#미완성된 내용이야

import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
from konlpy.tag import Okt

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori


#==========연관분석 그래프
def show_me_the_graph(df):
    import networkx as nx
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm

    g = nx.Graph()
    g.add_edges_from(df)
    pr = nx.pagerank(g)
    nsize = np.array([v for v in pr.values()])
    nsize = 10000 * (nsize - min(nsize)) / (max(nsize) - min(nsize))
    pos = nx.kamada_kawai_layout(g)
    font_name = fm.FontProperties(fname="./NanumMyeongjoBold.ttf").get_name()
    plt.figure(figsize=(16, 12))
    plt.axis("off")
    nx.draw_networkx(g, font_family=font_name, font_size=16,
                     pos=pos, node_color=list(pr.values()), edge_color='.5', node_size=nsize,
                     alpha=0.7, cmap=plt.cm.Blues)
    plt.show()

okt = Okt()
keyword = "코딩"
encoded = par.quote(keyword)
code = req.urlopen("https://www.joongang.co.kr/search/news?keyword={}".format(encoded))
soup = BeautifulSoup(code, "lxml")
news = soup.select("h2.headline a")

dataset = []
for i in news:
    print("제목 :",i.text)
    dataset.append(okt.nouns(i.text))
dataset_2 = []
for data in dataset:
    data_with_stopwords = []
    for noun in data:
        if len(noun) != 1:
            data_with_stopwords.append(noun)
    dataset_2.append(data_with_stopwords)

# print(dataset_2)
te = TransactionEncoder()
te_transform = te.fit(dataset_2).transform(dataset_2)
df = pd.DataFrame(te_transform, columns=te.columns_)
df_apr = apriori(df, use_colnames=True, min_support=0.06) #apriori는 기본적으로 0.5이상만 나오게 초기값으로 잡혀있었어
# print(df_apr)

#------------- 시각화
df_apr["length"] = df_apr["itemsets"].str.len() #원소 개수를 구하자
df_result = df_apr[df_apr["length"] == 2]["itemsets"]
# print(df_result)
show_me_the_graph(df_result)

