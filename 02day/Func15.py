# Func15.py
def pow(x): return x**2

a = [1,2,3,4,5,6,7,8,9,10]
b = list(map(pow,a))
print(b)

c = list(map(lambda x:x*100,a))
print(c)

d = [ i + 100 for i in a ]
print(d)
# a에서 짝수값만 제곱값, 홀수는 그대로  --> LC 형태
e = [ i**2 if i%2==0 else i for i in a  ]; print(e)
# a에서 짝수값만 제곱값, 홀수는 그대로 --> map 함수
f = list(map(lambda i:i**2 if i%2 == 0 else i,a)); print(f)

# a에서 홀수값만 원래값:제곱값 --> LC 형태
g = { i:i**2 for i in a if i%2 }; print(g)
# a에서 짝수는 원래값:제곱값 , 홀수는 원래값:0 --> LC 형태
h = dict(map(lambda i:(i,i**2) if i%2 == 0 else (i,0),a)); print(h)

# Filter( )

y = [1,2,3,4,5,6,7,8,9,10,15,20]

def f1(x): return (x>5) and ( (x%2)==1 )
#z = list(filter(f1,y))
z = list(filter(lambda x : (x>5) and  (x%2)==1,y))
print(z)



