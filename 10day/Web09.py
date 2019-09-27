# Web09.py
    # Naver.com 에서 [메일 카페 블로그 지식iN 쇼핑 Pay]
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = urlopen(url)
bs_obj = BeautifulSoup(html,'html.parser')

# <li class="an_item">
#bs1 = bs_obj.html.body.findAll('li',{"class":"an_item"})
#print(bs1)

bs2 = bs_obj.html.body.findAll('span',{"class":"an_txt"})
for span in bs2 : print(span)
bs3 = [span.text for span in bs2]
print(bs3)