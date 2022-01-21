import pandas as pd

df_merge = pd.DataFrame()
company = ["LG전자", "삼성전자","현대자동차"]

for i in company:
    df = pd.read_excel("./엑셀/광고비_{}.xlsx".format(i))
    df.set_index("date", inplace=True) #data 열을 인덱스로 지정하겠다 변한값을 내부적으로 하겠다
    df_merge[i] = df["total"] #df의 total열의 값들을 df_merge[회사이름]열에 들어가게되
df_merge.to_excel("./엑셀/광고비_토탈.xlsx")