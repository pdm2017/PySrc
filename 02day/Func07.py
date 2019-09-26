# Func07.py
def pSum(*j,s):
    r = 0
    for i in j: r = r+i
    return (s+ ' ' + str(r))

print(pSum(20,10,s='덧셈')) # 덧셈 30
print(pSum(20,10,5,s='덧셈')) # 덧셈 35
print(pSum(20,10,5,2,s='덧셈')) # 덧셈 37

a = [10,20,30,40,50]
print(pSum(*a,s='덧셈')) # 덧셈 150
