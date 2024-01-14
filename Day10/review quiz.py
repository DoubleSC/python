import random

# num=[]
#
# for i in range(10):
#     num.append(random.randint(1,100))
#
# print(num)
#
# num_even = []
# num_odd=[]
#
# for i in num:
#     if i % 2 == 0:
#         num_even.append(i)
#     else:
#         num_odd.append(i)
#
# print(num_even)
# print(num_odd)

num=[]
zoolist=[]

for i in range(10):
    num.append(random.randint(1,30))

for i in num:
    if i >= 1 and i <= 10:
        zoolist.append('토끼')
    elif i>=11 and i <= 20:
        zoolist.append('원숭이')
    else:
        zoolist.append('개')

print(zoolist)

def makelist(m,n):
    return [random.randint(m,n+1) for i in range(5)]

lambda m,n: [random.randint(m,n+1) for i in range(5)]



