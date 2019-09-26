# for07.py
# List Comprehension -> 중첩 반복문
m1 = ["A","B","O"]
w1 = ["A","B","O"]

c1 = [ i+j for i in m1 for j in w1 ]
print(c1)

c2 = [[ i+j for i in m1 ] for j in w1 ]
print(c2)
