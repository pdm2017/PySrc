# Book07.py

class Book :
    def __init__(self,t,a,p):
        self.__title__ = t # public
        self.__author_ = a # private --> 메소드 우회접근
        self.__price = p   # private --> 메소드 우회접근
        self.category = '' # 방치 (public)

b1 = Book("파이썬","홍길동",30000)


