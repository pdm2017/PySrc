# Web06.py
# HTML_example3.html
from bs4 import BeautifulSoup
html = open('HTML/HTML_example3.html','r',encoding='utf-8')
bs_obj = BeautifulSoup(html,'html.parser')
# print(bs_obj)

# 책제목만 출력
#print(bs_obj.html.body)
#pTags = bs_obj.html.body.findAll('p',{"id":"book_title"})
#print(pTags)
titles = [t.text for t in bs_obj.html.body.findAll('p',{"id":"book_title"})]
authors = [t.text for t in bs_obj.html.body.findAll('p',{"id":"author"})]
# print(titles); print(authors)
#books = { titles[i]:authors[i] for i in range(len(titles))}
books = dict(zip(titles,authors))
print(books)



