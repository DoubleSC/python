num = int(input("숫자 입력 : "))
num_list = list(map(int,str(num)))

num_list_reversed = list(reversed(num_list))
num

print(num_list_reversed)


phone_num = input("핸드폰번호입력 : ")
passwordNumber = ""

for index, item in enumerate(phone_num):
    if len(phone_num) - index > 4 :
        passwordNumber += "*"
    else:
        passwordNumber += item


print(passwordNumber)

