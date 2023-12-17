my_birth_year = int(input("당신이 태어난 연도는?"))
print(f"당신의 만나이는 {2023-my_birth_year}세 입니다.")

num1 = int(input("첫번째 숫자는?"))
num2 = int(input("두번째 숫자는?"))
num3 = int(input("세번째 숫자는?"))

print(f"세 숫자의 평균은 {(num1+num2+num3)/3} 입니다.")

krw = int(input("당신이 보유한 원화는 얼마입니까?"))
today_usd_krw = float(1304)
today_yen_krw = float(919.90)

print(f"당신이 보유한 원화의 달러환산 금액은 {krw/today_usd_krw}USD 입니다.")
print(f"당신이 보유한 원화의 엔화환산 금액은 {krw/today_yen_krw*10}엔 입니다.")

km_mile = float(0.621371)
km = int(input("킬로미터 거리는?"))

print(f"당신이 입력한 킬로미터는 {km * km_mile}마일입니다.")

celi = float(input("현재 섭씨 몇도입니까?"))

print(f"현재 온도는 화씨 {celi*59+32}도 입니다.")

height = float(input("당신의 키는?"))
weight = float(input("당신의 몸무게는?"))

print(f"현재 당신의 bmi 지수는 {weight/(height*height)}도 입니다.")
