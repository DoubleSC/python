movie_dic = {
   1:{
       'name':'일반영화',
       'price':10000,
       'seat':'일반석',
       'seat price':0,
       'snack': '기본콤보',
       'snack price':3000,
   },
   2:{
       'name':'3D영화',
       'price':12000,
       'seat':'프리미엄석',
       'seat price':3000,
       'snack': '프리미엄콤보',
       'snack price':5000,
   },
   3:{
       'name':'4DX영화',
       'price':15000,
       'seat':'VIP',
       'seat price':5000,
       'snack': 'VIP콤보',
       'snack price':8000,
   },
}

movie = int(input("원하는 영화는?(1.일반 2.3D, 3.4DX)"))
seat= int(input("원하는 좌석은?(1.일반, 2.프리미엄, 3.VIP)"))
snack=int(input("원하는 간식은?(1.기본, 2. 프리미엄, 3VIP)"))
age=int(input("나이 : "))

if age<=12:
    print(f"{(movie_dic[movie]['price']+ movie_dic[seat]['seat price']+ movie_dic[snack]['snack price'])*0.5}원 입니다.")

elif age>12 and age<=18:
    print(f"{(movie_dic[movie]['price'] + movie_dic[seat]['seat price'] + movie_dic[snack]['snack price']) * 0.8}원 입니다.")

elif age>=65:
    print(f"{(movie_dic[movie]['price'] + movie_dic[seat]['seat price'] + movie_dic[snack]['snack price']) * 0.7}원 입니다.")

else:
    print(f"{(movie_dic[movie]['price'] + movie_dic[seat]['seat price'] + movie_dic[snack]['snack price'])}원 입니다.")

print(f"{movie_dic[movie]['name']},{movie_dic[movie]['price']},{movie_dic[seat]['seat']},{movie_dic[seat]['seat price']},{movie_dic[snack]['snack']},{movie_dic[snack]['snack price']}")