# Num02.py
import numpy as np
d1 = list(range(1,13))
print(d1) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
a1 = np.array(d1).reshape(2,6)
print(a1)
a2 = np.array(d1).reshape(3,2,2)
print(a2)

print(a1.shape,a1.ndim,a2.shape,a2.ndim)
##############################################

a3 = np.array(list(range(1,7))).reshape(2,3)
print(a3)
print(a3.shape,a3.ndim)

a4 = np.zeros(6).reshape(2,3)
print(a4)

a5 = np.zeros(8*8).reshape(8,8)
print(a5)

a6 = np.ones(9).reshape(3,3)
print(a6)

a7 = np.eye(5);
print(a7)

import random as rd
r1 = rd.randint(1,10); print(r1)

a8 = np.random.randn(1,3); print(a8) # (시작점,끝점) --> 1개의 값
a8 = np.random.rand(1,3); print(a8)  # 0 ~ 1 (,개수) <-- 표준정규분포
a8 = np.random.randint(1,3); print(a8) # 0 ~ 1 (,개수) <-- float 수

a9 = np.array(list(range(1,13))).reshape(2,6)
a9 = np.array(range(1,13)).reshape(2,6)
a9 = np.arange(1,13).reshape(2,6)
print(a9)

a10 = np.array([1,2,3,4,5],dtype=np.float)
print(a10,a10.dtype)
a10 = np.array([1,2,3,4,5],dtype=np.float64)
print(a10,a10.dtype)
a10 = np.array([1,2,3,4,5.0],dtype=np.int)
print(a10,a10.dtype)
a10 = np.array([1,2,3,4,5.0],dtype=np.int64)
print(a10,a10.dtype)

a11 = np.arange(1,7).reshape(2,3)
print(a11,a11.dtype)
a12 = a11.astype(np.float64)
print(a12,a12.dtype)

a13 = a11.astype(np.str) # <-- str : U
print(a13,a13.dtype)

a13 = a11.astype(np.string_) # <-- str : S
print(a13,a13.dtype)

a14 = np.array(['tom','Alice','Hong','jane','Sophia'])
print(a14,a14.dtype) # <U5          --> Sophia ==> <U6
a15 = a14.astype(np.string_) # ==> str (unicode)
print(a15,a15.dtype) # |S5         --> Sophia ==> |S6

a14 = np.array(['tom','Alice','홍길동','jane'])
print(a14,a14.dtype) # <U5
#a15 = a14.astype(np.string_)
# UnicodeEncodeError: 'ascii' codec can't encode characters
#print(a15,a15.dtype)
