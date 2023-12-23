today_to_do = input("오늘 해야할 일은 무엇인가요?")
today_feel = input("오늘 기분은 어떠신가요?")

print(f"오늘 당신이 해야할 일은 {today_to_do}이고 기분은 {today_feel}이시군요!")

excersise1 =input("당신이 원하는 운동 첫번째는 무엇인가요?")
excersise2 =input("당신이 원하는 운동 두번째는 무엇인가요?")
excersise3 =input("당신이 원하는 운동 세번째는 무엇인가요?")

print(f"이상적인 운동순서는 {excersise1},{excersise2},{excersise3}이네요.")

circle = int(input("원의 반지름의 길이는?"))

print(f"반지름 {circle}cm인 원의 넓이는 {3.14* circle **2}, 둘레는 {3.14*2*circle}입니다.")

usd_bitcoin = float(input("현재 달러 대비 비트코인은 얼마입니까?"))
usd = int(input("현재 보유하신 달러는?"))

print(f"보유하신 달러는 {usd/usd_bitcoin} 비트입니다.")

movie = ['인셉션','서울의 봄','노량','범죄도시']
snack = ['팝콘','감자칩','핫도그','오징어']
drink = ['커피','콜라','사이다','아이스티']

pick1 = int(input("인셉션, 서울의봄, 노량, 범죄도시 중 선호하는 영화는?(0~3번)"))
pick2 = int(input("팝콘, 감자칩, 핫도그, 오징어 중 선호하는 간식은?"))
pick3 = int(input("커피, 콜라, 사이다, 아이스티 중 선호하는 음료는?"))

print(f"오늘의 영화선택은 {movie[pick1]}, 간식은 {snack[pick2]}, 음료는 {drink[pick3]} 이군요!")
