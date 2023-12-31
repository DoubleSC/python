#미니 퀴즈
# 유저한테 양의 정수를 입력 받고
# 0~ 양의 정수
# 0 ~n까지의 합을 나타내는 프로그램

# num = int(input("아무숫자 입력 : "))+1
# sum = 0
# for x in range(num):
#     sum = sum + x
#
# print(sum)

# num = int(input("0~100까지의 숫자 입력: "))
# sum = 0
#
# for x in range(101):
#     if x % num ==0:
#         sum = sum + x
#
# print(sum)

# 모음제거 프로그램

# word = input("아무영단어 : ")
# text = word
#
# for x in word:
#     if x in 'aeiou':
#         text = text.replace(x,"")
#
# print(text)

#1. num = []랜덤 정수(0~10000)를 100개 채우기
#2. num의 평균 값 도출하기

# import random

# num = []
#
# for x in range(100):
#     num.append(random.randint(0,10000))
#
# num_sum = sum(num)
# print(f"{num_sum/100}")

# import random
#
# num=[]
#
# for x in range(10):
#     num.append(random.randint(0,100))
#
# print(num)
#
# double_num=[]
# for i in num:
#     double_num.append(i**2)
#
# print(double_num)

# for index,item in enumerate("asdasdasdgasdg"):
#     print(index,item)
#
# for n in range(1,10):
#     if n == 5:
#         break
#     print(n)
#
# for n in range(1,10):
#     if n %2==0:
#         continue
#     print(n)

# while(무한 루프)

# a=1
# while a < 10:
#     print(a)
#     a += 1
#
# while True:
#     num = int(input("숫자를 입력(0은 종료):"))
#     if num == 0:
#         break
#

import random

# a = random.randint(0,101)
# try_num = 0
# while True:
#     num = int(input("0~100까지의 숫자중 한 숫자를 입력해주세요 : "))
#     if num > a:
#         print("down")
#         try_num += 1
#     elif num<a:
#         print("up")
#         try_num += 1
#     elif num==a:
#
#         print(f"정답입니다! 정답은 {a}입니다. 때려맞춘 횟수는 {try_num}번 입니다.")
#         break

# a_list=[]
#
# while True:
#     a = int(input("0을 입력하기 전까지 여러 정수를 입력해주세요"))
#     a_list.append(a)
#     if a == 0:
#         print(f"{sum(a_list)}")
#         break

# 일본여행 todolist

# 1. 먹고싶은 리스트
#  1) 먹고싶은 것은?
# 2. 가고 싶은 리스트
#  2) 가고싶은 곳은?
# 3. 리스트 보기
#  1) 먹고싶은 리스트:[], 가고 싶은 곳 리스트:[]
# 4. 종료

# food_list = []
# place_list = []
# time = 0
#
# while True:
#     code = int(input("1. 먹고싶은 리스트추가 2. 가고싶은 곳 리스트 추가 3. 리스트 보기, 4.종료 "))
#     if code == 1:
#         food = input("뭐 드시고 싶으세요: ")
#         food_list.append(food)
#     elif code == 2:
#         place = input("어디 가고 싶으세요: ")
#         place_list.append(place)
#     elif code == 3:
#         print(f"먹고싶은 리스트는 {food_list}, 가고싶은 곳 리스트는 {place_list}입니다. ")
#     elif code == 4:
#         print("프로그램 종료!")
#         break

#더하기 빼기 프로그램
plus = 0
minus = 0

while True:
    code = int(input("1. 더하기 숫자 입력해주세요. 2. 빼기 숫자를 입력해주세요. 3. 종료"))
    if code == 1:
        user_num = int(input("첫번째 더하기 숫자 입력해주세요"))
        user_num1= int(input("두번째 더하기 숫자 입력해주세요"))
        print(f"더한 값은 {user_num+user_num1}입니다.")

    elif code == 2:
        user_num2 = int(input("빼기 숫자 입력해주세요"))
        user_num3 = int(input("두번째 더하기 숫자 입력해주세요"))
        print(f"빼기 값은 {user_num2-user_num3}입니다.")

    elif code == 3:
        print("프로그램 종료!")
        break








