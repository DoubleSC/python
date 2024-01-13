# print([i for i in range(21) if i % 2 ==0])
#
# print([a for a in range(1,11) if a > 5])
#
# list = ["apple","banana","cherry","date"]
#
# print([word[0] for word in list])
#
# print([i**2 for i in range(1,6)])

my_string = input("단어를 입력해주세요")
reverse_my_string = ''

for word in my_string:
    reverse_my_string=word+reverse_my_string

print(reverse_my_string)

todolist = ['programming','sleeping','game','eating']
finished = [True, True, False, False]
havetolist = []

for index,item in enumerate(finished):
    if not item:
        havetolist.append(todolist[index])

print(havetolist)


