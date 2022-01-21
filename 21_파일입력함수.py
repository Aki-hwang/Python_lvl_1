
# "r" 모드의 특징 : 존재하지 않으면 에러를 보여줘

f = open("test.text", "r")
# result = f.readline()
result = f.readlines()
f.close()
print(result)