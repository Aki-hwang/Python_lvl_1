import pandas as pd


write = pd.ExcelWriter("./엑셀/장사시설현황_합치기.xlsx") #시트 네임을 넣기 위해 write 사용
for year in range(2017,2021):
    df = pd.read_excel("./엑셀/장사시설현황_2017년_2020년/{}년 장사시설 현황/전국장사시설현황.xlsx".format(year),sheet_name="장례식장 시설정보")
    # print(df[["시설명","주소"]])
    df[["시설명", "주소"]].to_excel(write, sheet_name="{}년".format(year))
write.save()