# Func03.py

# 숫자를 입력받아서 그 숫자만큼 * 를 출력하는 함수 작성
def pStar1(n):
    for i in range(n):
        print('*',end='')
    print()
#print('*'*5)
#print('^*^-'*5)
#def pStar1(n):


pStar1(5) #==> *****
pStar1(3) #==> ****

# 숫자를 입력받아서 그 숫자만큼 문양을 출력하는 함수 작성
def pStar2(n=5,s='$'):
    for i in range(n):
        print(s,end='')
    print()

pStar2(5,'*') #==> *****
pStar2(3,'@') #==> @@@
pStar2(4) #==> $$$$
pStar2() #==> $$$$$
