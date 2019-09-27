# Web10.py

import urllib.request
import bs4

url = "http://news.naver.com/"
html = urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, "html.parser")

hdline = bs_obj.find_all("div", {"class":"hdline_article_tit"})
for line in  hdline:
    print(line.text.strip())
