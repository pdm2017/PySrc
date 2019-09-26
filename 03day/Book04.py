# Book04.py

class Book:
    category = '소설' # Class 멤버

b1 = Book(); print(b1.category)
b2 = Book(); print(b2.category)
print(Book.category)
Book.category = '수필'
print(Book.category)
print(b1.category)
print(b2.category)