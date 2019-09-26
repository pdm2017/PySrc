# Re01.py
import re
a1 = 'pizza'; a2 = 'banana'; a3 = 'az' ; a4 = 'sk'

r = re.compile("[az]")
print(r.search(a1))
print(r.search(a2))
print(r.search(a3))
print(r.search(a4))

if not r.search(a4): print('a나 z 가 없어요')