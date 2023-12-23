# # 1. 대문자화 소문자화
# a = 'megastudy'
# b = a.upper()
# c = a.lower()
# print(b)
# print(c)
#
# # 2. all 대문자 입니까? all 소문자 입니까?
#
# x = b.islower()
# y = c.isupper()
#
# print(x)
# print(y)
#
# # 3. 공백제거
# marriage = "오늘 결혼식 추카 "
#
# marriageStrip = marriage.strip()
# print(marriageStrip)
#
# # 4. split (리스트화)
# con = "오늘 결혼 축하해!"
# con_Split = con.split()
#
# con2 = "오늘! 결혼! 축하해!"
# con2_Split = con2.split("!")
#
# print(con_Split)
# print(con2_Split)

# 5. replace(대체)
# news = 'In the ever-evolving lan'
# news_replace = news.replace("In","at")

# print(news_replace)

#6. find(찾기)

# find = news.find("lan")
# print(find)

#7. startswith(시작), endswith(끝)

#8. join(연결)
# menu = ['아아','라떼','디카페인']
# join = '존맛 '.join(menu)
# print(join)

# words = input("꿀잼?")
# news = """이번주 수도권 지역 중 전주 대비 아파트 매매가격이 상승한 지역이 한 곳도 없는 것으로 집계됐다"""
# replace_news = news.replace(" ",words)
#
# print(replace_news)
#
# # 9. is 시리즈
# # isdigit(), isalpha(), isalnum()
#
# # 10. count
# # 단어 세주기
#
# a=news.count("이")
# print(a)