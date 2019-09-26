# Func04.py
def Sum(*n): # 가변길이 매개 변수
    ans = 0
    for i in n: ans += i
    return ans

print(Sum(20,10))       # 30
print(Sum(20,10,5))     # 35
print(Sum(20,10,5,3))   # 38
print(Sum(20,10,5,3,2))   # 40

b = [10,20,30,40]
print(Sum(*b))

print(Sum(*[10,20,30,40]))