# def func1():
#     a = 1 #지역번수 : 함수 안에서 만들어져서 함수 안에서만 접근이 가능
#
# func1()
# # print(a)
# #전역번수 : 함수 밖에서 만들어진 변수 함수내에서 리드만 가능 수정 불가능해 (파이썬에서만)
num = 10

def func2():
    global num #전역변수 num 수정 허락 받기
    num += 1
    print(num)

func2()