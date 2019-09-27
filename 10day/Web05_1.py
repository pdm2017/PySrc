# Web05_1.py

# HTML_li2.html 파일 오픈
from bs4 import BeautifulSoup
html = open('HTML/HTML_li2.html','r')
bs_obj = BeautifulSoup(html,'html.parser')
#print(bs_obj)

html2 = bs_obj.findAll('div')
#print(html2)
for t in html2 :
    li = t.find('ul').findAll('li')
    for l in li :
        print(l.text)



