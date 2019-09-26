# Str01.py

a1 = 'sk'
a2 = 'sk'
print (a1 == a2)
print ( a1 is a2)
print(id(a1),id(a2))

a3= ['hp','sk','lg']
print(id(a1),id(a2),id(a3[1]))

#
#print("입력하세요 --> sk")
#a4 = input()
#print(id(a1),id(a4))
#print(a1==a4,a1 is a4)

b1 = 'sk'
b2 = 'sk'
b3 = b1
b4 = b1[:]
print(id(b1),id(b2),id(b3),id(b4))

c1 = ['hp','sk','lg']
c2 = ['hp','sk','lg']
c3 = c1
c4 = c1[:]
print(id(c1),id(c2),id(c3),id(c4))
