score=int(input("점수:"))

dig={10:'A',9:'A',8:'B',7:'C',6:'D',5:'F',4:'F',3:'F',2:'F',1:'F',0:'F'}
if score >= 0 and score <= 100:
    if score//10>=9:
        print(score,":",dig[10])
    elif (score//10)==8:
        print(score,":",dig[8])
    elif score //10==7:
        print(score,":",dig[7])
    elif score//10==6:
        print(score,":",dig[6])
    elif score//10<=5:
        print(score,":",dig[5])

    else:
        print("입력 가능한 점수의 범위는  0~100입니다")
