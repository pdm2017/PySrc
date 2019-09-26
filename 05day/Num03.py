# Num03.py
# 연산
import numpy as np
ar1 = np.array([1,2,3,4,5],dtype=np.float64)
ar2 = np.array([4,5,6,7,8],dtype=np.int32)
ar3 = ar1 + ar2
print(ar3, ar3.dtype)
print(ar1-ar2)
print(ar1*ar2)
print(ar1/ar2)

# 같은 위치(요소)끼리 연산됨
# 계산되는 array의 모양(구조)가 동일해야 함
ar4 = np.array([[1,2,3],
                [4,5,6]],dtype=np.float64)
ar5 = np.array([[9,8,7],
                [6,5,4]],dtype=np.float64)
print(ar4+ar5)
print(ar4-ar5)
print(ar4*ar5)
print(ar4/ar5)
#########################3
# ar1 = np.array([1,2,3,4,5],dtype=np.float64)
print(ar1+3)
print(ar1*2)
print(ar1**2)
print(10/ar1)
print('='*20)

#ar4 = np.array([[1,2,3],
#                [4,5,6]],dtype=np.float64)
print(ar4+3)
print(ar4*2)
print(ar4**2)
print(10/ar4)

# Broadcast
ar6 = np.array([[1,2],[3,4]])
ar7 = np.array([10,20])
print(ar6+ar7)
print(ar6*ar7)

ar8 = np.array([[1,2],
                [3,4]])
ar9 = np.array([[2,3],
                [4,5]])

print(ar8+ar9)
print(ar8**ar9)
print(np.matmul(ar8,ar9)) # matrix mul

ar10 = np.arange(1,13).reshape(3,2,2)
print(ar10,ar10.max(), ar10.min(), ar10.mean(),ar10.sum())

ar11 = np.arange(1,7).reshape(2,3)
print(ar11)
ar12 = ar11.T # shape 가로축 <--> 세로축 변환
print(ar12)
print(np.matmul(ar12,ar11)) # matrix mul