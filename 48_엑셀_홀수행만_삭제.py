import openpyxl
import pandas as pd #라이브러리 자동 설치 커서위에 놓고 알트 + 엔터 + 엔터

df = pd.read_excel("./엑셀/전자기기매출액.xlsx") #데이터 프레임이라는 자료형으로 가져오게 하는거야
df[::2].to_excel("./엑셀/전자기기짝수행만.xlsx", index=None) #인덱스 번호를 지우기 위해 index = none을 사용

#엑셀과 궁함도 좋아서 많이 쓰거든
# print(df[10:21]) #10번째에서 21번째 행만 가져오겠다
# print(df[:])#모든행열 가져오겠다
# print(df[::2]) #모든행을 가져오는데 짝수행만



