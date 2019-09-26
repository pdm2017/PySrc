# Collections01.py

# from 폴더 import 파일
# from 파일 import 항목

from collections import deque

q1 = deque()
print(type(q1),q1)
for i in range(5): q1.append(i+1)
print(q1)
q1.pop()
print(q1)
q1.insert(0,10)
print(q1)
q1.appendleft(20)
print(q1)

