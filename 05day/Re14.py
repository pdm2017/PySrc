import re
print(re.search("\d","우기는 1994년에 입대하였습니다"))
print(re.search("\d+","우기는 1994년에 입대하였습니다"))
print(re.match("\d+","우기는 1994년에 입대하였습니다"))
print(re.match("\d+","1994년에 우기는 입대하였습니다"))
print(re.findall("\d+","우기는 1994년에 5월 31에 입대하였습니다"))
print(re.split("[:]+","사과 귤 : 포도 토마토"))
print(re.split("[: ,]+","사과 귤 : 포도, 토마토"))
print(re.sub("-","**","123-456-7890"))
