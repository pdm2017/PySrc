# test01.py

a = 10
print(a)

############################
a = [10,20,30,[40,50,60],70,80]
b = [10,20,30,[40,[50,60],70],80,90]
# a,b 의 길이는?
print(len(a),len(b))
# a 에서 40,50,60 출력
print(a[3]) # 인덱싱
print(a[-3])# 인덱싱
# a 에서 50,60 출력
print(a[3][1:]) # 슬라이싱
# a 에서 60,70 출력
print(a[3][2],a[4])

b = [10,20,30,[40,[50,60],70],80,90]
# b 에서 30 ~ 70 출력
print(b[2:4])
print(b[2:-2])
# b 에서 60,70 출력
print(b[3][1][1],b[3][2])

########################################
c = ['A','B','A','B','C','B','A']
# c 에서 중복제거후, 튜플로 저장하세요 (sorting)

d = tuple(sorted(list(set(c))))
print(d) # ('A','B','C')

########################################
a = (10,20,30); print(type(a),a)
b = 10,20,30; print(type(b),b)
c = 10, ; print(type(c),c)
d = (10,) ; print(type(d),d)
e = 'A', ; print(type(e),e)
f = 10,'A',[11,22], ; print(type(f),f)
g = () ; print(type(g),g)
h = (10) ; print(type(h),h)

########################################
a = (10,20,30,40,50)
b = 60,70
c = 80,
print(a+b+c)
d = 80,90,
print(c,d)

########################################

a = ['사과','배','토마토']
b = '사과','배','토마토'
# a , b 에서 '배'를 '포도' 로 변경해보세요
a[1] = '포도'; print(a)

b1,b2,b3 = b; # tuple unpacking
b2 = '포도';
b = b1,b2,b3; # tuple packing
print(b)

c = 10,20,30
# c의 모든 숫자를 1씩 증가하세요 --> 11,21,31
c1,c2,c3 = c
c = c1+1,c2+1,c3+1
print(c)

d = 10,20,30
# d의 모든 값의 뒤에 'd'를 추가하세요 --> '10d','20d','30d'
d1,d2,d3 = d
d = str(d1)+'d',str(d2)+'d',str(d3)+'d'
print(d)

s1 = {1,2,3,4,5}
s2 = {1,3,5,7,9}
# print(s1+s2)

print(s1 & s2); print(s1.intersection(s2))
print(s1 | s2); print(s1.union(s2))
print(s1 - s2); print(s1.difference(s2))
print(s1^s2)

# z1 = []; z2 = (); z3= ; z4 = {}
z1 = list(); z2 = tuple(); z3= set(); z4 = dict()
print(type(z1),type(z2),type(z3),type(z4))

