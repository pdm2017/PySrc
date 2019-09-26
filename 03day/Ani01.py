# Ani01.py
# 동물병원
# 개(이름,운다()), 고양이(이름,운다())
class Animal: # (object)
    def __init__(self):
        self.name = '이 름'
    def cry(self): return '운 다'

class Dog(Animal): pass
class Cat(Animal): pass
class Duck(object): pass

d1 = Dog(); c1 = Cat()
print(d1.name, d1.cry(), c1.name, c1.cry())
k1 = Duck();


