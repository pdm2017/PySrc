# Func08.py

a = 7

def Sum(i,j):
    # a = 9 # local 지역 변수
    global a # glocal 전역 변수
    r = i + j + a
    return r

print(Sum(10000,2000))

#########################
def test(i):
    global b
    b = i

b = 0
test(200)
print(b) # 200