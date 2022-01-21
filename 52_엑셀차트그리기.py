import openpyxl
from openpyxl.chart import Reference, Series, LineChart, BarChart


company = ["LG전자", "삼성전자", "현대자동차"]
for i in company:
    book = openpyxl.load_workbook("./엑셀/광고비_{}.xlsx".format(i))
    sheet = book.active
    # 차트 만들기
    chart = BarChart()
    chart.title = " {}월별 광고비".format(i)
    for j in ["C", "D", "E", "F", "G"]:
        value = Reference(sheet, range_string="Sheet1!{}2:{}13".format(j,j))
        value_series = Series(value, title=sheet["{}1".format(j)].value)
        chart.append(value_series)
    sheet.add_chart(chart, "J1")
    book.save("./엑셀/광고비_{}_차트.xlsx".format(i))