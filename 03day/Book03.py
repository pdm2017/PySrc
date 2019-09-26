# Book03.py
# Book : title, author, price
class Book :
    def __init__(self,*args):
        self.title = '무제' if len(args)<1 else args[0]
        self.author = '작자미상' if len(args)<2 else args[1]
        self.price = 0 if len(args)<3 else args[2]
    def pBook(self):
        print(self.title,self.author,self.price)

b1 = Book("파이썬","홍길동",30000)
b1.pBook()
b2 = Book("자바","김연아")
b2.pBook()
b3 = Book()
b3.pBook()
#b4 = Book(price = 200)
#b4.pBook()

