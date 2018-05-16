items={"라면":650, "우유":1100,"콜라":1200,"캔커피":500,"과자":700}

while True:
    it=input("상품명:")
    if  it:
       print ([it,":",items[it]], ">", items[it])

    elif it==key:
        break

    else:
        print(it,"는 미등록 제품입니다.")

print("[%s:%d] > %d"%(it,items[it],s))
