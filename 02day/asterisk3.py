# asterisk3.py
def asterisk_test_2(*args):
    x, y, *z = args
    return x, y, z

print(asterisk_test_2(3, 4, 5))

def Calc(x,y): return x+y, x-y,x*y,x/y

a,b,c,d = Calc(200,100)
print(a,b,c,d)

def test01(*args):
    #a,b,c,d,e,f = args
    a, b ,c , *d = args
    return [a,b,c],d

points = [100,50,70,80,70,90]
print(test01(*points))
alice,tom = test01(*points)
print(alice); print(tom)

b= [1,2,3,4,5,6,7]
c,d,*e =  b
print(c,d,e)

# stu1 의 data 를 받아 학생의 총점 평균 출력

def pPoint(*args):
    name,*p = args
    total = 0
    for i in p : total += i
    print("{} 총점:{}, 평균:{}".format(name,total,total/len(p)))

stu1 = ['jane',60,70,80]; stu2 = ['alice',100,67,78,89]
stu3 = ['tom',99,55,60,70,80]
pPoint(*stu1); pPoint(*stu2); pPoint(*stu3)
##################################################
def pPoints(args):
    for s in args: pPoint(*s)

students = [stu1,stu2,stu3]
pPoints(students)
