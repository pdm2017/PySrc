# type01.py
a = 10; print(type(a)) # ==> int a = new int(10);
a = 'sk'; print(type(a))
a = 3.14; print(type(a))
a = 3+4j; print(type(a))
a = False; print(type(a))
#######################################

b1 = 0; b2=''; b3 = []; b4 = (); b5 = {}; b6 = False; b7 = None
print(bool(b1),bool(b2),bool(b3))
print(bool(b4),bool(b5),bool(b6),bool(b7))

# if not 0 ; if not ''; if [] ; if () ; if {} ; if None

x = 10; x = None
print(type(x),x)

if not x : print("x 에 data가 연결되어 있지 않아요")
x = 10;
if x : print("x 에 data가 연결되어 있어요")

y1 = 'sk'; y2 = '''sk'''; y3 = "sk"; y4 = """sk""";

y5 = '''<font color='red'>sk 하이닉스</font>'''
y6 = '''select * from emp where ename = 'tom' '''
print(y5)

z = '20190916Mon'

date = z[:8]
day = z[8:]
print(date,day)

print("일시 : {0}, 요일 : {1}".format(date,day))
print("일시 : {}, 요일 : {}".format(date,day))

print("일시 : %s, 요일 : %s" % (date,day) )



