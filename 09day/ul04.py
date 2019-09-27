# ul04.py
from bs4 import BeautifulSoup
with open('Web/Test02.html','r',encoding="utf-8") as f1:
    bs = BeautifulSoup(f1,"html.parser")

body_tag = bs.find('body')
tag_list = body_tag.find_all(['p','img'])
for tag in tag_list: print(tag)