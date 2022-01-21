import random

ans = random.randint(1,10) #1~100사이에 랜덤한 숫자를 뽑음

print("업다운 게임을 시작합니다")
cnt = 0
while True:
    num = int(input("숫자를 입력하세요>>>"))
    cnt += 1
    if num == ans :
        print("정답입니다")
        break
    elif num > ans:
        print("Down")
    elif num < ans:
        print("Up")
print("{}회만에 정답을 맞추셨습니다".format(cnt))


#내가 만든것
# while True:
#     num1 = int(input("숫자를 입력하세요>>>"))
#     if num1 > ans:
#         print("다운입니다")
#     elif num1 < ans:
#         print("업입니다")
#     if num1 == ans:
#         print("정답입니다")
#         break