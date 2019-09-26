# Book06.py
class Book:
    category = '소설'         # class 멤버 속성
    def __init__(self):
        self.title = '무제'   # instance 멤버 속성
    def pBook(self):
        print(self.title)       # instance 멤버 메소드
    @classmethod
    def pCate(cls):
        print(Book.category)  # class 멤버 메소드
    @staticmethod
    def test():                 # static 멤버 메소드
        print("이것은 static 멤버 메소드")
#########################################################
b1 = Book(); b2 = Book()
print(b1.title,b2.title)
b1.pBook(); b2.pBook()

print(Book.category,b1.category,b2.category)
Book.category = '수필'
print(Book.category,b1.category,b2.category)
Book.pCate()

Book.test()





