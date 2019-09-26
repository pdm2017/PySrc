# Ani04.py
class Animal(object):
    # object 기본 생성자 오버라이드
    def __init__(self,n,a):
        self.name = n
        self.age = a
    # object 기본 함수 오버라이드
    def __str__(self): return "{}의 나이는 {}살".format(self.name,self.age)
    # object 기본 연산자 오버라이드
    def __add__(self, other): #  self + other
        return self.name + ',' + other.name

class Dog(Animal): pass
class Cat(Animal): pass

a1 = Animal('해피',10); print(a1) # 해피의 나이는 10살
a2 = Animal('아치',20); print(a2)
d1 = Dog('뽀삐',7); print(d1)
c1 = Cat('양이',3); print(c1)

print(d1+c1)