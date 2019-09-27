# ul03.py
from bs4 import BeautifulSoup
with open('Web/Test01.html','r',encoding="utf-8") as f1:
    bs = BeautifulSoup(f1,"html.parser")

pList = bs.find_all('p')
for p in pList: print(p)
print(bs.find('head').find('title'))
#print(bs.prettify())