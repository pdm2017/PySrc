# Ani03.py
class A:
    def __init__(self): print("class A 실행")
    def test1(self):print('A')
    def testA(self): print('testA')
class B:
    def __init__(self): print("class B 실행")
    def test1(self):print('B')
    def testB(self): print('testB')
class C:
    def __init__(self): print("class C 실행")
    def test1(self):print('C')
    def testC(self): print('testC')

class D(B,C,A):
    def __init__(self):
        super().__init__()

d1 = D(); d1.test1(); d1.testA(); d1.testB(); d1.testC()
