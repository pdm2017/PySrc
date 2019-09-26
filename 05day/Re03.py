# Re03.py
import re
url = '<a href="C:\Python\Apple.jpg"> 사과  </a><font size="10">'
print(re.search('href="(.*?)">',url).group(1))

a = 'testTomtest' # ==> Tom 만 추출
print(re.search('test(.*?)test',a).group(1))

b = '<font color="red.txt"> <br>' # ==> red.txt 만 추출
print(re.search('color="(.*?)"',b).group(1))
