# Web04_1.py
import bs4
#from bs4 import BeautifulSoup

html_str = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
# bye 뽑아내기
aaaa = bs_obj.findAll("li")

li_text = [a.text for a in aaaa if 'o' in a.text]
print(li_text)

# Li 태그 단어 중 영문 o 가 있는 것만 추출



