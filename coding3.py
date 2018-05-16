score=int(input("점수:"))

if score >= 0 and score <= 100:
    if score <= 100 and score >= 90:
        print(score,":","A")
    elif score < 90 and score >= 80:
        print(score,":","B")
    elif score < 80 and score >= 70:
        print(score,":","C")
    elif score < 70 and score >= 60:
        print(score,":","D")
    elif score < 60 and score >= 0:
        print(score,":","F")

    else:
        print("입력 가능한 점수의 범위는  0~100입니다")
