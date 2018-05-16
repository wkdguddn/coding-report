items={"라면":650, "우유":1100,"콜라":1200,"캔커피":500,"과자":700}

s=0
it=input("제품명:")
while True:
    
    if  it in items:
       s=s=+items[it]
       print("[%s:%d] > %d"%(it,items[it],s))
       it =input("제품명:")

    elif it !="" and it not in items:
        print(it,"는 미등록 제품입니다.")
        it=input("제품명:")
        continue


    elif it=="":
        break

print("총금액:",s)
    


