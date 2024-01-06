# b = []
#
# for i in ["hello","world","python","programming"]:
#     b.append(len(i))
#
# print(b)
#
# #
# word_list = ["apple","banana","cherry","date"]
# b = []
# #
# # for i in a :
# #     b.append(i[0])
# #
# # print(b)
#
# for word in word_list:
#    newWord = ""
#    for spell in word:
#        if not spell in 'aeiou':
#            newWord += spell
#            b.append(newWord)
#
# print(b)

food_list=[]
place_list=[]
shopping_list=[]

while True:
    code=int(input("1)일본에서 먹고 싶은 음식리스트 추가, 2)일본에서 가보고 싶은 곳 리스트 추가, 3)일본에서 쇼핑하고 싶은 리스트 추가, 4)리스트 모아보기, 5)리스트 종료"))
    if code == 1:
        food=input("일본에서 먹고 싶은 음식 : ")
        food_list.append(food)
    elif code == 2:
        place = input("일본에서 가보고 싶은 곳 : ")
        place_list.append(place)
    elif code == 3:
        shop = input("일본에서 사고 싶은것 : ")
        shopping_list.append(shop)
    elif code == 4:
        print(f"일본에서 먹고싶은 음식 리스트는 {food_list}, 가보고 싶은 곳의 리스트는 {place_list}, 사고 싶은 것의 리스트는 {shopping_list}입니다.")
    elif code == 5:
        print("프로그램을 종료합니다")
        break
    else:
        print("잘못입력하셨습니다")


