# Web08.py
# naver.com 에서 '네이버를 시작페이지로'를 가져와서 출력

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = urlopen(url)
bs_obj = BeautifulSoup(html,'html.parser')
# <div class="area_links">
#bs1 = bs_obj.html.body.find('div',{"class":"area_links"})
#print(bs1)
#   <a class="al_favorite" ~~~
bs2 = bs_obj.find('a',{"class":"al_favorite"}).text
print(bs2)