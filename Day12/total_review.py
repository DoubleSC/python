# 제어문
# 조건문 : if, elif, else

# 반복문 : for, while
#     for - range, 문자열, 리스트
#     while - 무한루프
#     break, continue문- 반복문을 제어 했음.

# 컴프리헨션(리스트, 딕셔너리 단축화)
# [i for i in range/str/list] - 기본형
# [i for i in range/str/list if i % 2 == 0] - filter 형
# [피자 if i % 2 == 0 else 햄벅 for i in range/str/list] - map 형
#
# zip화
# coffeelist = ['a','b','c'], priceList = [1000,2000,3000]
# zip(coffeeList, priceList) # ('a',1000),('b',2000), ('c',3000)
# [{'이름'}]
#
# 일반함수
#
# def name(arg):
#     ...
# return ...
#
# 람다함수
# lambda x : x
#
# 콜백함수
# 함수의 매개변수에 함수를 넣어줌
# function some(x[콜백함수])
#
# map(변형), fliter(필터), reduce(누적)