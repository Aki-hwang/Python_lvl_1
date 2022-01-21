#
# phonelist = []
# numOfData = 0
# while True:
#     print("=====================")
#     print("현재 데이터 개수 : {}".format(numOfData))
#     print("1. 전화번호 추가")
#     print("2. 전화번호 검색")
#     print("3. 전화번호 삭제")
#     print("4. 전화번호 전체 출력")
#     print("5. 종료")
#     print("=====================")
#     selectNumber = int(input("선택 >>"))
#     if selectNumber == 1:
#         name = input("이름 : ")
#         number = input("전화번호 : ")
#         phonelist.append({"name" : name, "number" : number})
#         numOfData += 1
#     elif selectNumber == 2:
#         search_name = input("이름 : ")
#         se_name = False
#         for data in phonelist:
#             if search_name == data["name"]:
#                 print("이름 :", data["name"])
#                 se_name = True
#             elif se_name == False:
#                 print("찾는 이름이 없습니다")
#     elif selectNumber == 3:
#         delete_name = input("이름 : ")
#         se_name = False
#         for data in phonelist:
#             if delete_name == data["name"]:
#                 phonelist.remove(data)
#                 numOfData -= 1
#                 se_name = True
#                 print("이름이 삭제되었습니다.")
#             elif se_name == False:
#                 print("찾는 이름이 없습니다")
#     elif selectNumber == 4:
#         for data in phonelist:
#             print("--------------------")
#             print("이름 : ", data["name"])
#             print("전화번호 : ", data["number"])
#             print("--------------------")
#     elif selectNumber == 5:
#         print("전화번호부를 종료합니다")
#         break
#

phonelist = []
f = open("./phone_book.text", "r")
data = f.readlines() #한줄씩 받아
for i in data:
    print(i.strip()) #strip() 문자열 양끝에 있는 공백, 개행문자를 지워줌 문자열 자료형에만 쓸수 있어
    i = i.split(",") #split(",") 콤마를 기준으로 값을 나눈후 리스트형으로 반환
    phonelist.append({"name": i[0], "number":i[1]})

numOfData = len(phonelist)

def inputData():
    name = input("이름 : ")
    number = input("전화번호 : ")
    phonelist.append({"name": name, "number": number})
    f = open("./phone_book.text","a")
    f.write(name + "," + number + "\n")
    f.close()
    global numOfData
    numOfData += 1
def searchData():
    search_name = input("이름 : ")
    se_name = False
    for data in phonelist:
        if search_name == data["name"]:
            print("이름 :", data["name"])
            se_name = True
        elif se_name == False:
            print("찾는 이름이 없습니다")
def deleteData():
    delete_name = input("이름 : ")
    se_name = False
    for data in phonelist:
        if delete_name == data["name"]:
            phonelist.remove(data)
            numOfData -= 1
            se_name = True
            print("이름이 삭제되었습니다.")
        elif se_name == False:
            print("찾는 이름이 없습니다")
def printData():
    for data in phonelist:
        print("--------------------")
        print("이름 : ", data["name"])
        print("전화번호 : ", data["number"])
        print("--------------------")
while True:
    print("=====================")
    print("현재 데이터 개수 : {}".format(numOfData))
    print("1. 전화번호 추가")
    print("2. 전화번호 검색")
    print("3. 전화번호 삭제")
    print("4. 전화번호 전체 출력")
    print("5. 종료")
    print("=====================")
    selectNumber = int(input("선택 >>"))
    if selectNumber == 1:
        inputData()
    elif selectNumber == 2:
        searchData()
    elif selectNumber == 3:
        deleteData()
    elif selectNumber == 4:
        printData()
    elif selectNumber == 5:
        print("전화번호부를 종료합니다")
        break