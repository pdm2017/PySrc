# Web01_1
# HTML_example3.html
from bs4 import BeautifulSoup
html = open('HTML/HTML_example3.html','r',encoding='utf-8')
bs_obj = BeautifulSoup(html,'html.parser')
# print(bs_obj)
css_select1 = bs_obj.select("body p")
#print(css_select1)
css_select2 = bs_obj.select("body p#book_title")
#print(css_select2)
titles = [t.text for t in bs_obj.select("body p#book_title")]
authors = [t.get_text() for t in bs_obj.select("body p#author")]
books = dict(zip(titles,authors))
print(books)