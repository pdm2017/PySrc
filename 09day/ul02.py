# ul02.py
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = urlopen("https://www.daum.net")
bs = BeautifulSoup(url,"html.parser")

# class="img_thumb
cList = bs.select('.img_thumb')
for c in cList: print(c)
#alt1 = bs.find_all(alt="삼성닷컴")
#print(alt1)

#imgLists = bs.find_all('img')
#for img in imgLists: print(img)

# print(bs.prettify())