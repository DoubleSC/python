# Comprehension : 리스트, 딕셔너리, 세트와 같은 자료구조들을 생성하는데 간결하고 효율적인 문법
# 파이썬에서의 리스트 컴프리헨션은 for 문을 사용하여 리스트를 생성하는 간결하고 효율적인 방법입니다.
# 기본적인 for 문 대신에 리스트 컴프리헨션을 사용하면 코드를 더 짧고 읽기 쉽게 만들 수 있습니다.

# double_num = [i**2 for i in range(9)]
# print(double_num)
#
# num_3 = [i+3 for i in range(10)]
# print(num_3)
#
# num_even = [i for i in range(9) if i % 2 ==0]
# print(num_even)

# num_range = int(input("정수의 범위 : "))+1
# num_1 = int(input("범위내의 정수 첫번째 : "))
# num_2 = int(input("범위내의 정수 두번째 : "))
#
# num_list = [i for i in range(1,num_range) if i % num_1 == 0 and i % num_2 ==0]
# print(num_list)

# word = ['coffee','cookie','sandwich']
#
# word_number = [len(i) for i in word]
# print(word_number)

# news = """Bharat Ramamurti, Senior Adviser for Economic Strategy at the American Economic Liberties Project, discusses Job numbers,
#  if the US could be in a soft landing and how a shutdown could affect the Economy. He spoke to Kailey Leinz on Bloomberg Radio.
# """
#
# news_list = [i for i in news.split() if i.isalpha() and len(i) >= 6]
# news_list.sort()
#
# print(news_list)

# 조건문 심화

# print([i if i % 2 == 0 else 'A' for i in range(101)])

# print(['🙏' if str(i%10) in '369' or str(i//10) in '369' else i for i in range(1,101)])

news = """Bharat Ramamurti, Senior Adviser for Economic Strategy at the American Economic Liberties Project, discusses Job numbers,
 if the US could be in a soft landing and how a shutdown could affect the Economy. He spoke to Kailey Leinz on Bloomberg Radio.
"""

# news_list = news.split()
# news_list_2 = [i.upper() if len(i)>=5 else i.lower() for i in news_list if i.isalpha]
# print(news_list_2)

#중첩 루프 컴프리헨션

# 컴프리헨션 내에서 두개 이상의 반복문을 중첩하여 사용할 수 있습니다. 이는 여러 개의 리스트나 다른 반복가느안 객체들 간의 조합을 생성하는 데 유용합니다.

# print([i+j for i in range(3) for j in range(3)]) # 모든 경우의 수가 나올때까지 리스트에 담김
#
# print([f"{i}*{j}={i*j}" for i in range(2,10) for j in range(2,10)])

# celsius = [0,10,20,30,40]
#
# print([f"{i*9/5+32}" for i in celsius ])

print([i for i in range(0,101) if i % 2 == 0])