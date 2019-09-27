# ul01.py
from bs4 import BeautifulSoup
f1 = open('Web/Test00.html','r',encoding='utf-8')
#fdata = f1.read()
bs = BeautifulSoup(f1,"html.parser")
f1.close()
print(bs.find('h1'))
#print(bs.prettify())
#print(fdata)