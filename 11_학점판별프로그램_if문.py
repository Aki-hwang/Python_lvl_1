score = int(input("점수입력 >>>"))
if score >= 90:
    print("학점 A") # tab한번으로 진행
elif 80 <= score <90:
    print("학점 B")
elif 70 <= score <80:
    print("학점 C")
else:
    print("학점 F3")
