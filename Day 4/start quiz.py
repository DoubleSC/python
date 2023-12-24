exc = input("당신이 좋아하는 운동 5가지:(띄어쓰기 필수)")

excer_list = exc.split()
excer_list.sort()
print(excer_list)

news = """그는 이재명 더불어민주당 대표에게 이낙연 전 대표 집으로 찾아가는 방식으로 노무현 전 대통령의 길을 가야 한다고 촉구했다고 강조했다.
앞서 지난 21일 박 전 원장은 CBS 라디오 ‘김현정의 뉴스쇼’에 나와 이 같은 내용을 피력한 바 있다."""

word = input("검색하고 싶은 단어:")
word_count = news.count(word)
print(word_count)


e_mail = input("이메일 주소를 입력해주세요")
e_mail_split = e_mail.split("@")
print(e_mail_split)

ran = input("아무문자열을 입력해주세요")
ran2 = sorted(ran)
ran3 = ' '.join(ran2)

print(ran3)


