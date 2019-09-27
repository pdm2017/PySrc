# Web04_2.py
from bs4 import BeautifulSoup
# HTML_Li 파일 오픈
html = open('HTML/HTML_li.html','r')
bs_obj = BeautifulSoup(html,'html.parser')
#print(bs_obj)

ul = bs_obj.findAll("ul",{"class":"reply"})
print(ul)