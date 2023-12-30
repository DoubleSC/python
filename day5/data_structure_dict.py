# 자료구조 (data_structure)- dict
# key[정수, 문자]
# coffee = {
#     # 'key':'value'
#     1: '아메리카노',
#     2: '라떼',
#     3: '바닐라',
# }
#
# nation = {
#     '한국': '서울',
#     '일본': '도쿄',
#     '중국': '베이징',
#     '프랑스': '파리',
# }
#
# japan_travel = {
#     'city': ['후쿠오카', '벳푸', '나가사키', '히로시마'],
#     'food': ['라멘', '초밥', '텐동'],
#     'hotel': [
#         {'이름': '퍼스트스테이', '가격': 100000, '조식': False},
#         {'이름': '신라스테이', '가격': 120000, '조식': False},
#     ]
#
# }
#
# mbti = input("당신의 MBIT를 입력해주세요:")
# lowerMBTI = mbti.lower()
# mbti_dic = {
#     'e': '외향적',
#     'i': '내향적',
#     's': '현실적',
#     'n': '직관적',
#     't': '이성적',
#     'f': '감성적',
#     'j': '계획적',
#     'p': '즉흥적'
# }
# print(lowerMBTI)
#
# print(f"당신은 {mbti_dic[lowerMBTI[0]], mbti_dic[lowerMBTI[1]], mbti_dic[lowerMBTI[2]], mbti_dic[lowerMBTI[3]]} 이군요")
#
# movie = int(input("원하시는 영화는? 1:액션, 2:로맨틱코미디, 3:공포 "))-1
# age = int(input("나이가 어떻게 되시나요? "))
#
#
# set_movieage = {
#     'price':[10000,8000,9000]
#     }
#
# if age < 13:
#     print((f"당신이 원하는 영화의 가격은 {set_movieage['price'][movie]*50/100}이군요"))
# elif age >= 13 and age < 60:
#     print((f"당신이 원하는 영화의 가격은 {set_movieage['price'][movie]*100/100}이군요"))
# else:
#     print((f"당신이 원하는 영화의 가격은 {set_movieage['price'][movie]*70/100}이군요"))

# movie ={
#     1:{
#         'name':'액션 영화',
#         'price':10000
#             },
#     2: {
#         'name': '로맨틱 코메디 영화',
#         'price': 8000
#     },
#     3: {
#         'name': '공포 영화',
#         'price': 9000
#     }
# }
#
# movie_number = int(input("영화를 고르세요(1.액션 2.로코 3.공포):"))
# age = int(input("나이를 입력하세요:"))
#
# if age < 13:
#     print(f"고르신 영화는 {movie[movie_number]['name']} 가격은 {movie[movie_number]['price']*0.5}원 입니다.")
# elif age >= 13 and age < 60:
#     print(f"고르신 영화는 {movie[movie_number]['name']} 가격은 {movie[movie_number]['price']*1.0}원 입니다.")
# else:
#     print(f"고르신 영화는 {movie[movie_number]['name']} 가격은 {movie[movie_number]['price']*0.7}원 입니다.")


bus = {
    1:{
        'name':'시내버스',
        'price':1200
    },
    2:{
        'name':'광역버스',
        'price':2000
    },
    3:{
        'name':'마을버스',
        'price':1000
    },
}

bus_num = int(input("원하시는 버스타입을 알려주세요(1:시내버스, 2:광역버스, 3: 마을버스)"))
age = int(input("나이를 입력해주세요 : "))

if age<7:
    print(f"선택하신 버스노선은 {bus[bus_num]['name']}이고 가격은 {bus[bus_num]['price']*0}원 입니다.")

elif age>=7 and age<20:
    print(f"선택하신 버스노선은 {bus[bus_num]['name']}이고 가격은 {bus[bus_num]['price'] * 0.7}원 입니다.")

elif age >= 65:
    print(f"선택하신 버스노선은 {bus[bus_num]['name']}이고 가격은 {bus[bus_num]['price'] * 0}원 입니다.")

else:
    print(f"선택하신 버스노선은 {bus[bus_num]['name']}이고 가격은 {bus[bus_num]['price'] * 1.0}원 입니다.")

