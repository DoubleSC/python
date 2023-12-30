# a = input("안녕하세요. 문자 한개를 입력해주세요!")
#
# if a.isalpha:
#     print("알파벳입니다!")
# else:
#     print("알파벳이 아니에요!")

# num = int(input("숫자를 말씀해주세요!"))
# if num % 2 == 0:
#     print("짝수입니다.")
#
# else:
#     print("홀수입니다.")

# import random
#
# answer = random.randint(1,20)
#
# a = int(input("숫자 입력:"))
# if a < answer:
#     print("up!")
# elif a > answer:
#     print("down!")
# else:
#     print("정답입니다!")
#
# kor = int(input("국어점수:"))
# math = int(input("수학점수:"))
# eng = int(input("영어점수:"))
# avg = (kor + math + eng)/3
#
# if avg > 90:
#     print("A")
# elif avg > 80:
#     print("B")
# elif avg > 70:
#     print("C")
# elif avg > 60:
#     print("D")
# else:
#     print("낙제입니다")

list = ['아메리카노','레몬에이드','카페라떼']
price = [3000,4000,3500]
num = int(input("원하시는 음료를 선택해주세요(0:아메리카노,1:레몬에디드,2:카페라떼)"))
pay = int(input("지불금액을 입력해주세요:"))

americano = int(3000)
lemon = int(4000)
latte = int(3500)

if price[num] > pay:
    print("지불금액을 더 투입하세요")
else:
    print(f"원하시는 음료는 {list[num]}이고 잔돈은 {pay-price[num]}입니다.")




