# for02.py

a = [0,1,2,3,4,5,6,7,8,9]
b = list(range(0,10,1))
print(b)
c = list(range(100))
print(c)
d = list(range(100,0,-1))
print(d)

e = [ i*i for i in range(1,11)]
print(e)

e = [ i*i for i in range(1,11) if(((i*i)%2) == 1) ]
print(e)

e = [ i*i for i in range(1,11) if not (i*i)%2 ]
print(e)

f = { i:i**2 for i in range(1,11)}
print(f) # ==> {1:1,2:4,3:9,4:16,,,,,10:100}

for _ in range(7): print(_,end=' ')