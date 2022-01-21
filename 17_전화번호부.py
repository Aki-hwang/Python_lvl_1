phoneList = []
numOfData = 0
while True:
    print("====================")
    print("현재 데이터 개수 : {}개".format(numOfData))
    print("1. 전화번호 추가")
    print("2. 전화번호 검색")
    print("3. 전화번호 삭제")
    print("4. 전화번호 전체출력")
    print("5. 종료")
    print("====================")
    menu = int(input("선택 >>>"))
    if menu == 1:
        name = input("이름 입력 : ")
        number = input("번호 입력 : ")
        phoneList.append({"name":name, "number":number})
        numOfData += 1
    elif menu == 2:
        search_name = input("검색할 이름 입력 >>>")
        is_find = False
        for data in phoneList:
            if data["name"] == search_name:
                print("---------------------")
                print("이름 : ", data["name"])
                print("번호 : ", data["number"])
                print("---------------------")
                is_find = True #포문을 모두 돌았을때 같은 이름이 있는 경우 True
        if is_find == False:
            print("찾는 이름이 없습니다")
    elif menu == 3:
        delet_name = input("삭제할 이름 입력 >>>")
        is_find = False
        for data in phoneList:
            if data["name"] == delet_name:
               phoneList.remove(data)
               numOfData -= 1
               is_find = True  # 포문을 모두 돌았을때 같은 이름이 있는 경우 True
        if is_find == False:
            print("찾는 이름이 없습니다")
    elif menu == 4:
        for data in phoneList: #for문은 리스트 자료형이 좋아
            print("---------------------")
            print("이름 : ", data["name"])
            print("번호 : ", data["number"])
            print("---------------------")
    elif menu == 5:
        print("프로그램을 종료합니다")
        break
    else:
        print("올바른 선택이 아닙니다")
