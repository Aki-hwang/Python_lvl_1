import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

dataset = [  #리시트 자료형
    ["사과", "치즈", "생수"],
    ["생수", "치즈", "호두", "고등어"],
    ["사과", "옥수수","복숭아"],
    ["생수", "치즈", "호두", "옥수수"]
]


te = TransactionEncoder()
te_transform = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_transform, columns=te.columns_)
# print(df)
df_apr = apriori(df, use_colnames=True)
print(df_apr)
