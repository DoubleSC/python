# 함수 정의 방법 : def 키워드
# 파이썬에서 함수는 def 키워드를 사용하여 정의합니다. 이후 함수 이름과 괄호 안에 매개 변수를 기술하고, 콜론(:)으로 함수의 본문을 시작합니다.
# 이 예시에서 my_function은 함수의 이름이며, Param1과 Param2는 매개변수입니다.

# def my_function(param1, param2):
#     result= param1+param2
#     return result
#
# # 함수 호출 및 실행 과정
# print(f"{my_function(1,2)}")

#
# def triangle(a,b):
#     area = a * b / 2
#     return area
#
# print(f"정삼각형의 넓이는 {triangle(2,4)}")
#
# def square(c):
#     area2 = c ** 2
#     return area2
#
# print(f"정사각형의 넓이는 {square(2)}")
#
# def circle(l,flag):
#     if flag:
#         return l ** 2 * 3.14
#     else:
#         return l * 2 * 3.14
#
# print(f"{circle(2,4)}")
#
# def maratang(*topping):
#     toplist = []
#     for i in topping:
#         toplist.append(i)
#     print(f"{toplist} 마라탕 완성!")
#
# maratang(*topping='당면','새우','두부','라면')

# 단일 값 변환

# def square(number):
#     return number * number
#
# result = square(4)
# print(result)
#
# # 다중 값 변환(튜플 사용)
#
# def get_user():
#     name = "Alice"
#     age = 25
#     return name, age
#
# user_name, user_age = get_user()
# print(user_name)
# print(user_age)

# retrun 문이 없는 경우는 None 표시

#함수의 범위와 생명주기

# 지역변수와 전역 변수
# 변수의 범위
# 생명주기



