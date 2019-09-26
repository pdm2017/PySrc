# Func12.py
'''
1 @ 4 = 17
3 @ 4 = 25
2 @ 7 = 53
4 @ 8 = 80
'''
# 중첩 함수 
def Test(x,y) :
    def Sum(i,j): return i+j
    def Pow(i): return i**2
    return Sum(Pow(x),Pow(y))
    
    
print(Test(1,4)) # 17
print(Test(3,4)) # 25
print(Test(2,7)) # 53
print(Test(4,8)) # 80
