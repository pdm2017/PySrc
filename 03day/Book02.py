# Book02.py
class Book:
    def __init__(self,t='무제',a='미상',p=0):
        self.title = t # instance 멤버
        self.author = a
        self.price = p
    def pBook(self): print(self.title, self.author, self.price)

b1 = Book(); b1.pBook()
b2 = Book("java"); b2.pBook()
b3 = Book("sql","tom"); b3.pBook()
b4 = Book("python","jane",30000); b4.pBook()