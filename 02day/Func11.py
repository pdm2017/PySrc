# Func11.py
def calc(x,y):
    return x+y,x-y,x*y,x/y

print(calc(20,10))
a,b,c,d = calc(20,10)
print(a,b,c,d) # 덧셈,뺄셈,곱셈,나눗셈

def swap(i,j): return j,i

x = 200
y = 100
x,y = swap(x,y)
print(x,y) # 100,200

x,y = y,x
print(x,y)


