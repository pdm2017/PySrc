# Web07.py
# HTML_example_my_site.html
from bs4 import BeautifulSoup
html = open('HTML/HTML_example_my_site.html','r',encoding='utf-8')
bs_obj = BeautifulSoup(html,'html.parser')
# a > class='portal' 출력
# print(bs_obj)
bs1 = [a.text for a in bs_obj.html.body.findAll('a',{"class":"portal"})]
print(bs1)                                      # 태그,{속성:값}

bs2 = [a.text for a in bs_obj.select('a.portal')] # class 명
print(bs2)

bs3 = [a.text for a in bs_obj.select('a#google')] # id 명
print(bs3)

