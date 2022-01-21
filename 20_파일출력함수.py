#파일열기모드
# W 모드 : 쓰기 모드,
# 파일이 존재 하지 않으면 생성
# 파일의 내용을 모두 지운 후에 파일을 열어

# "a" 모드 : 더해서 쓰기모드
# 파일이 존재 하지 않으면 생성
# 파일의 내용을 모두 유지한 후 파일을 연다


f = open("test.ppt", "w")
f.write("Hello\n")
f.write("World\n")
f.write("Python\n")
f.close()