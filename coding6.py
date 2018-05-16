engkor_dict = dict() 

eng = input("영어 단어 : ")

kor = input("한글 단어 : ") 

while True : 

     if eng != "": 
        engkor_dict[eng] = kor 
        eng = input("영어 단어 : ") 
        kor = input("한글 단어 : ") 

    elif eng =="" and kor == "": 
       break 

 
print(engkor_dict) 
