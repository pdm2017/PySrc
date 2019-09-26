# Ani07.py
from abc import ABCMeta,abstractmethod
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def cry(self): pass

class Dog(Animal):
    def cry(self): print('멍멍')
class Cat(Animal):
    def cry(self): print('야옹')
class Duck(Animal):
    def cry(self): print('꽥꽥')

aList = [Dog(),Cat(),Duck()]
for a in aList: a.cry()