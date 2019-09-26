# Book01.py

# 서점 => 책(제목, 저자, 가격)
class Book:
    # 멤버 생성자
    def __init__(self): # <-- 메모리 로드, 함수 호출 
        self.title = '무제'  # 멤버 변수/속성
        self.author = '미상'
        self.price = 0
    # 멤버 메소드
    def pBook(self): print(self.title, self.author, self.price)

b1 = Book(); b1.title="java"; b1.author='tom';b1.price = 30000
b1.pBook()
b2 = Book(); b2.title="sql"; b2.author='alice';b2.price = 40000
b2.pBook()
b3 = Book(); b3.title="java"; b3.author='jane';b3.price = 20000
b3.pBook()

print(b1 is b3)
print(b1.title is b3.title)
print(id(b1.title),id(b3.title))

print(dir(Book))