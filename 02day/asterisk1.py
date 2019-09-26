# asterisk1.py
def asterisk_test(a, b, *args):
    return a + b + sum(args)

print(asterisk_test(1, 2, 3, 4, 5))

def test01(*args, a, b ):
    return a + b + sum(args)
print(test01(1, 2, 3, a=4, b=5))

def test02(a, *args, b ):
    return a + b + sum(args)
#print(test02(1, 2, 3, a=4, b=5))
