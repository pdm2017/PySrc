# Func13.py
a = ['콜라','사이다','씨그램','우유','활명수'] #,'박명수']
b = [1000,900,600,700,800]

#for s in a : print(s)
#for i in range(len(a)): print(i,a[i])
# enumerate()함수
for i,s in enumerate(a): print(i,s)
# zip() 함수
c = list(zip(a,b)); d = dict(zip(a,b))
print(c); print(d)

#########################################

x = list(zip(a,b))
print(x)

#for i,(j, k) in enumerate(list(zip(a,b))): print(i,j,k)
for i,s in enumerate(zip(a,b)): print(i,s)
for i,(j, k) in enumerate(zip(a,b)): print(i,j,k)
