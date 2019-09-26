# Ani05.py
class Animal:
    def __init__(self,name = '무명'):
        self.name = name
    def __add__(self,other):
        return (self.name +' 와 ' + other.name + ' 입니다.')
    def __sub__(self,other):
        return (self.name +' 와 ' + other.name + '는 사이가 나빠요')
    def __iadd__(self,other):
        return (self.name +' 와 ' + other.name + '는 사이가 좋아요')
    def __gt__(self,other):
        return (self.name +' 는 ' + other.name + '보다 키가 커요')
class Dog(Animal) : pass
class Cat(Animal) : pass

c1 = Cat("아치")
d1 = Dog("해피")
print(c1.name,d1.name)
a1 = Animal('하이')
a2 = Animal('바이')
print(a1 + a2); print(a1 - a2); print(a1 > a2)
a1+=a2
print(a1)
