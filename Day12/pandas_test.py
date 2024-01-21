import pandas
import random

from faker import Faker

name = []
fake=Faker()
for i in range(300):
    name.append(fake.name())



age = []
for i in range(300):
    age.append(random.randint(10,70))


coffeelist = []
coffees=['americano','latte','decaffein','milklatte','vanilla','mocha','maxim']

for i in range(300):
    coffeelist.append(random.choice(coffees))

data = {
    'name' :name,
    'age' : age,
    'coffee' : coffeelist
}

df = pandas.DataFrame(data)

df.to_csv('megaCoffee.csv', index=False)

# 이름 : 300개
# 나이 : 10~70 랜덤으로
# 커피 : ['americano','latte','decaffein','milklatte','vanilla','mocha','maxim']




# data = {
#     'name' :['cho','son','lee','hwang','lee'],
#     'age' : [26,31,24,28,29],
#     'position' : ['cf','lw','rw','mf','mf']
# }
#
# df = pandas.DataFrame(data)
# print(df)
# df.to_csv('soccer.csv', index=False)

