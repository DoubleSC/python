# reduce : 누적

from functools import reduce

numList = [1,2,3,4,5]

result = reduce(lambda acc,cur: acc+cur,numList)
factorial = reduce(lambda acc,cur: acc*cur,numList)

print(result)
print(factorial)

