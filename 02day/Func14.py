# Func14.py

def sum(i,j): return i+j
def sub(i,j): return i-j
def mul(i,j): return i*j
def div(i,j): return i/j

a = sum
print(a(20,10))

cList1 = [sum,sub,mul,div]
for c in cList1: print(c(200,100),end=' ')
print()

rList1 = [c(2000,1000) for c in cList1]
print(rList1)

cList2 = []
cList2.append(sum)
cList2.append(sub)
cList2.append(mul)
#print(cList2)
for c in cList2: print(c(20000,10000),end=' ')
cList2.remove(sub)
for c in cList2: print(c(20000,10000),end=' ')
print()

# 람다식(Lambda)
# def div(i,j): return i/j
div = lambda i,j: i/j
print(div(40,10))

#nmj = lambda i,j: i%j

cList3 = [sum,sub,mul,div,lambda i,j: i%j]
print(cList3)
for c in cList3: print(c(22,11),end=' ')
print()


