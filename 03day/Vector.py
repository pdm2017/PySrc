# Vector.py
# Vector 표현
vector_list     = [1,2,10]
vector_tuple    = (1,2,10)
vector_dict     = {'x':1,'y':2,'z':10}

# Vector 연산
a1 = [1,2]
a2 = [3,4]
a3 = [5,6]
# 열단위 합계 ==> [9, 12]
r1 = []
for i in range(len(a1)):
    r1.append(a1[i]+a2[i]+a3[i])
print(r1)

print(list(zip(a1,a2,a3))) # [(1, 3, 5), (2, 4, 6)]
r2 = [ sum(t) for t in zip(a1,a2,a3) ]
print(r2)

a = [1,2,3,4,5]; print(sum(a))

# Vector 함수()
def v_add(*args): return [ sum(t) for t in zip(*args) ]

r3 = v_add(a1,a2,a3)
print(r3) # => [9, 12]

aRows = [a1,a2,a3]
r4 = v_add(*aRows) # <-- aRows
print(r4) # => [9, 12]
####################################
a1 = [1,2,3,4,5]
a2 = [3,4,5,6,7]
a3 = [5,6,7,8,9]
z1 = list(zip(a1,a2,a3)); print(z1)

a4 = [a1,a2,a3];
print(a4)
print(*a4)

#z2 = list(zip(a4)); print(z2)
#z3 = list(zip(*a4)); print(z3)