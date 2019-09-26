# Ani02.py
class Animal(object):
    aList = [ ]
    def __init__(self,n='이 름'):
        self.name = n
        self.aList.append(self.name)
    def cry(self): return '운 다'
    def shout(self): return '으 르 렁'

class Dog(Animal):
    def cry(self): return '멍 멍' # 메소드 오버라이드
class Cat(Animal):
    def cry(self): return '야 옹' # 메소드 오버라이드

d1 = Dog('해 피'); print(d1.name, d1.cry(),d1.shout(),Animal.aList)
c1 = Cat('아 치'); print(c1.name, c1.cry(),d1.shout(),Animal.aList)
