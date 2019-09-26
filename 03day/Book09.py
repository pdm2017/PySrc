# Book09.py

titles = ['java','c#','python','sql','db']
authors = ['tom','jane','alice','james','sophia']
prices = [30000,23000,45000, 19000,50000]

class Book:
    def __init__(self,t='무제',a='미상',p=0):
        self.title = t; self.author = a; self.price = p
    def pBook(self): print(self.title, self.author, self.price)

print(list(zip(titles,authors,prices)))
BookLists = [Book(t,a,p) for t,a,p in zip(titles,authors,prices)]
for b in BookLists: b.pBook()

