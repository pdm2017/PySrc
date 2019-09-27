# ul06.py
from bs4 import BeautifulSoup
with open('Web/Test04.html','r',encoding="utf-8") as f1:
    bs = BeautifulSoup(f1,"html.parser")
#print(bs.select('p')) # 태그 p
#print(bs.select('.name1')) # class .name1
#spanList = bs.select('div > p > span') # 상위태그 > 하위태그
#for span in spanList: print(span)

#  상위태그.class > 하위태그.class
#print(bs.select('p.name1 > span.store'))

# #아이디
print(bs.select('#fruits1'))