# Re13.py
import re
# \d --> 모든 숫자
print(re.search("\d+","감자는 6700원입니다."))
# \D --> 숫자를 제외한 모든 문자
print(re.search("\D","감자는 6700원입니다."))
# \w --> 모든 숫자 or 모든 문자
print(re.search("\w","감자는 6700원입니다."))
print(re.search("\w+","6700원은 감자의 가격입니다."))
# \W --> 모든 숫자와 모든 문자 제외
print(re.search("\W","감자는 6700원입니다."))
print(re.search("\W","6700원은 감자의 가격입니다."))

#############################

print(re.search("\d+","홍길동은 2001년 4월 27일에 태어남"))
print(re.findall("\d+","홍길동은 2001년 4월 27일에 태어남"))

print(re.search(":","사과 배 : 감 바나나"))
print(re.split(":","사과 배 : 감 바나나"))
print(re.split("[: ]","사과 배 : 감 바나나"))
print(re.split("[: ]+","사과 배 : 감 바나나"))

print(re.sub("//","/","http://www.test.co.kr"))

url = "http://www.daum.net http://www.naver.com"
url = re.sub("http://","/",url)
print(url)
url = re.split("[/ ]+",url)
print(url)
print(url[1:])

url2 = "http://www.daum.net http://www.naver.com"
print(re.split("[/ ]+",re.sub("http://","/",url2))[1:])
# ['www.daum.net','www.naver.com' ]

url3 = "http://www.daum.net http://www.naver.com"

print(re.split(" ",re.sub("http://","",url3)))