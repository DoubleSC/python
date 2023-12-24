# 1. 조건문
# if문

# toeic = int(input("토익 점수 입력:"))

# if toeic > 900:
#     print("축하합니다. 장려금이 나옵니다.")
#
# print("끝")
#
# # 중첩 if문
#
# if toeic > 800:
#     print("축하합니다.")
#     if toeic > 900:
#         print("장려금이 나옵니다!")

print("끝")

# elif, else문

# shopping = int(input("구매한 금액:"))
#
# if 50000> shopping and shopping >= 30000:
#     print("주차권 1시간!")
#
# elif 70000 >shopping and shopping >= 50000:
#     print("주차권 2시간!")
#
# elif 100000 >shopping and shopping >= 70000:
#     print("주차권 3시간!")
#
# elif shopping >= 100000:
#     print("주차권 종일!")
#
# else:
#     print("주차권 없음")


# Quiz : 수학점수
# 100~90 A
# 90~80 B
# 80~70 C
# 과락입니다.


math_score = int(input("수학점수:"))
korean_score = int(input("국어점수:"))
english_score = int(input("영어점수:"))

average_score = int((math_score+korean_score+english_score)/3)
print(f"평균점수는 {average_score}점입니다.")

if 80 > average_score and average_score >= 70:
    print(f"평균점수는 {average_score}점임으로 C등급입니다.")

elif 90 > average_score and average_score >= 80:
    print(f"평균점수는 {average_score}점임으로 B등급입니다.")

elif 100 >=average_score and average_score >= 90:
    print(f"평균점수는 {average_score}점임으로 A등급입니다.")

else:
    print(f"평균점수는 {average_score}점임으로 과락입니다.")

num = int(input("숫자:"))

if num > 0:

    if num % 2 == 0:
            print("양의 짝수입니다.")
    else:
            print("양의 홀수입니다")

elif num == 0:
    print("0")

else:
    if num%2 == 0:
            print("음의 짝수")
    else:
        print("음의 홀수")







