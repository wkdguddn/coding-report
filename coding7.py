engkor_dict = dict()

eng = input("영어 단어 : ")

while True:

    if len(engkor_dict) == 0 : 

        print("사전이 비어있습니다") 

        print("단어를 추가합니다") 

       kor = input("한글 단어 : ") 

       engkor_dict[eng] = kor 

      eng = input("영어 단어 : ") 

   elif len(engkor_dict) > 0 and eng not in engkor_dict and eng != "" : 

       print(eng,"단어가 등록되어 있지 않습니다.") 

       print("단어를 추가합니다") 

       kor = input("한글 단어 : ") 

       engkor_dict[eng]= kor 

      eng = input("영어 단어 : ")

    elif eng in engkor_dict :

        print(eng, ":" ,engkor_dict[eng])

        eng = input("영어 단어 : ")

    elif eng == "":

        break 

print(engkor_dict) 
