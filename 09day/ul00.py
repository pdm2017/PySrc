# ul00.py

from urllib.request import urlopen
url = 'http://www.skhynix.com'#'https://www.daum.net'
html = urlopen(url)
status = html.getheaders()
for s in status: print(s)
#print(status)
print(html.read())