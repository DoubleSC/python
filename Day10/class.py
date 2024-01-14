# 나만의 데이터 타입 만들기
# 기본형 -> 구조체 -> 클래스[class](구조체 + 함수)
# height[float] -> student[str, int]

class Dog:
    def __init__(self,x):
        self.name = x
        self.hp = 100
        self.emotionState = 'happy'
        self.hungry = 0
        self.friends = []

    def eating(self):
        if self.hp < 200:
            self.hp += 10

        else:
            print("체력이 꽉 찼습니다")

a = Dog('Jenny')
for i in range(100):
    print(f"{i}")
    a.eating()

print(f"{a.name},{a.hp}")


class Burger:
    def __init__(self,x,y):
        self.bread = x
        self.ingredients = y
        self.source = '마요네즈'

    def addIngredient(self,x):
        self.ingredients.append(x)

c=Burger('플랫프래드',['새우','애그마요'])
d=Burger('화이트',['패티'])

print(c.bread)
print(d.ingredients)

