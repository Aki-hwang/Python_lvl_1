import pandas as pd

df = pd.read_excel("./아파트분양가격.xlsx")
# print(df[df["분양가격"] >= 3000])
# print(df[df["지역명"] == "서울"])
# print(df[(df["지역명"] == "서울") & (df["분양가격"] >= 4000)])

print(df[(df["지역명"] == "서울") | (df["지역명"] == "제주")])  #또는


