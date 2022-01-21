fruit = {"사과" : 100, "포도" : 200, "배" : 300}
print(fruit["사과"])

fruit["오렌지"] = 500 #원소 추가하는 방법
print(fruit)

fruit.pop("사과") # 원소를 삭제
fruit["포도"] = 300 #원소를 수정