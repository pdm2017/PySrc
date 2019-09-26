# Func16.py
from functools import reduce
a = [1,2,3,4,5]

def f1(x,y): return x+y

b = reduce(f1,a); print(b)
c = reduce(f1,a[2:]); print(c)
d = reduce(f1,a[::2]); print(d)

# range(시작점,끝점,스텝)
# list대상 [ 시작점:끝점:스텝 ]
e = [11,22,33,44,55,66,77,88,99]
print(e[1:-2:2])
print(e[::3])