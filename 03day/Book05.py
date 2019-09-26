# Book5.py
class Book:
    bCnt = 0 # Class
    def __init__(self,t):
        Book.bCnt += 1
        self.title = t # instance 멤버

b1 = Book("java"); print(b1.title, b1.bCnt, Book.bCnt)
b2 = Book("sql"); print(b2.title, b2.bCnt, Book.bCnt)
b3 = Book("python"); print(b3.title, b3.bCnt, Book.bCnt)