# ul05.py
from bs4 import BeautifulSoup
import re
with open('Web/Test02.html','r',encoding="utf-8") as f1:
    bs = BeautifulSoup(f1,"html.parser")

#tags = bs.find_all(re.compile("^p"))
tags = bs.find_all(align="center")
print(tags)
txt = bs.find('p')
print(txt.string)

txt_list = bs.find_all('p')
for txt in txt_list:
    print(txt.string)

txt_list2 = bs.find_all('p')
for txt in txt_list2:
    print(txt.get_text())
