# Num04.py
import numpy as np
ar1 = np.array([[10,20],[30,40],[50,60]])
print(ar1,ar1.shape)
ar2 = ar1.flatten()
print(ar2,ar2.shape,type(ar2))

ar3 = np.arange(1,11)
print(ar3,type(ar3))
print(ar3[5])
print(ar3[2:-2])
print(ar3[5])

ar4 = np.arange(1,26).reshape(5,5)
print(ar4)
print(ar4[:])
print(ar4[:,:])
print(ar4[1][1]) # 다차원 List에서의 표현
print(ar4[1,1])  # 다차원 Array에서의 표현
print(ar4[1:3,1:3])
print(ar4[1:4,1:4])
print(ar4[:3,2:])
#ar5 = np.arange(1,126).reshape(5,5,5)
#print(ar5)

print(ar4[ar4%2==0])

ar5 = np.arange(1,101)
print(ar5)
# 3의 배수만 출력
print([i for i in ar5 if i%3==0])
print(ar5[ar5%3==0])
print(ar5[ar5>90])
# 50 보다 크고, 홀수인 숫자만 출력
print(ar5[(ar5>50)&(ar5%2==1)])

# ar4 -->
#[[ 1  2  3  4  5]
# [ 6  7  8  9 10]
# [11 12 13 14 15]
# [16 17 18 19 20]
# [21 22 23 24 25]]
# ar4 에서 3 x 3 영역만 0으로 바꿔서 ar6 에서 넣어보세요
print(ar4)
ar6 = ar4
ar6[1:4,1:4] = 0
print(ar6)

