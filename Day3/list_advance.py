# # list 함수
#
# menu =['🍔','🍟','🥯','🥩']
# menu.append('🍗')
# print(menu)
#
# # 리스트 연산자
# # 1. 덧셈 연산자(+)
# list_one = [1,2,3] + ['a','b','c','d']
# print(list_one)
#
# # 2. 곱셈 연산자 (*)
# list_two = ['넷플','티빙','유투브'] * 2
# print(list_two)
#
# # 3. 인덱싱
# list_three = ['신서유기','강식당','지구오락실']
# print(list_three[2])
#
# # 4. 슬라이싱
# list_four = ['메가커피','투썸','스벅','벤티']
# print(list_four[1:3])
#
# # 5. in, not in
# burger = ['버거킹','노브랜드','맘터','맥도날드']
# burger_in = '롯데리아' in burger
# burger_notin = '롯데리아' not in burger
# print(burger_in)
# print(burger_notin)
#
# # 1. append() 맨위에 추가
#
# coffee = ['아아','라떼']
# coffee.append('믹스커피')
# print(coffee)
#
# # 2. extend() + 리스트 추가 연산자와 같음
#
# ice_coffe = ['아이스 아메리카노','아이스 라떼']
# coffee.extend(ice_coffe)
#
# print(coffee)
#
# # 3. insert(어디에, 무엇을) 도중에 삽입
#
# coffee.insert(1,'콜드브루')
# print(coffee)
#
# # 4. remove(무엇을) 삭제
#
# coffee.remove('라떼')
# print(coffee)
#
# # 5. pop(몇번째) 안쓰면 맨 뒤에 삭제
#
# coffee.pop(3)
# print(coffee)
#
# # 6. clear 올삭제
#
# # 7. index(무엇을)
# coffee_index = coffee.index('믹스커피')
# print(coffee_index)
#
# # 8. count(무엇을) 몇개 있는지
#
# # 9. sort() 오름차순 정렬, 내림차순 sort(reverse=True)
#
# coffee.sort()
# print(coffee)
# coffee.sort(reverse=True)
# print(coffee)
#
# news = """베트남 정부가 제1외국어로 선정한 언어는 한국어를 제외하면 영어 중국어 일본어 프랑스어 러시아어 독일어가 전부입니다.
# 베트남에서 제1외국어는 초등학교3학년 때부터, 제2외국어는 중학교부터 선택과목으로 가르치는 언어입니다. 이전까지 한국어는 제2외국어에 속해있었지만,
# 2021년 초를 기점으로 제1외국어로 위상이 올라간 것입니다."""
# news_list = news.split()
# print(news_list)
#
# news_list.sort()
# print(news_list)

# 1. 운동 순서 저장 리스트
# 운동 루틴을 총 5개를 입력을 받고
# 오름차순으로 표현하는 프로그램

exc = input("운동 5가지를 골라주세요. 띄어쓰기 필수")
exc_list = exc.split()
exc_list.sort()

print(exc_list)


# 2. 뉴스를 가져와서 유저가 찾는 단어가 몇개인지 출력하는 프로그램

news = """베트남 정부가 제1외국어로 선정한 언어는 한국어를 제외하면 영어 중국어 일본어 프랑스어 러시아어 독일어가 전부입니다.
베트남에서 제1외국어는 초등학교3학년 때부터, 제2외국어는 중학교부터 선택과목으로 가르치는 언어입니다. 이전까지 한국어는 제2외국어에 속해있었지만,
2021년 초를 기점으로 제1외국어로 위상이 올라간 것입니다."""


word = input("찾고자 하는 단어는:")
news_count = news.count(word)

print(news_count)







