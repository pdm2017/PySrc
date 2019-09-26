# Pan01.py
# Pandas 라이브러리 : Data 분석 라이브러리
#       - Data Frame (Series) <-- List, Dict , Array
# Pandas : 코딩하는 엑셀
import pandas as pd
#print(pd.__version__)

# Series
a = [3,5,-1,4]
s1 = pd.Series(a)
print(s1,type(s1),s1.dtype)
print(s1.index)

b = ['A','B','D','C']; b1 = ['가','나','다','라']
s2 = pd.Series(b,index=b1)
print(s2,type(s2),s2.dtype)
print(s2.index)
print(s1[1],s2['나'])

c = {'Jane':80,'Tom':70,'Alice':90,'John':60}
s3 = pd.Series(c)
print(s3,type(s3),s3.dtype)
print(s3['Tom'])
print(s3.index)
print(s1.values,s2.values,s3.values)

s3.name = '학생점수'
s3.index.name='이름'
print(s3)

d = {'name':['Jane','Tom','Alice','John'], # list
     'age':[34,27,51,45], # list , tuple
     'point':[80,70,90,60]} # list
s4 = pd.Series(d)
print(s4,type(s4),s4.dtype)
print(s1[0]+s1[1]) # a = [3,5,-1,4] --> s1
print(s4['age'][0],s4['age'][1])
print(type(s4['age']),type(s4['point']))
print(type(s4['age'][0]),type(s4['age'][1]))
print(s4['age'][0]+s4['age'][1])

d = {'name':['Jane','Tom','Alice','John'],
     'age':[34,27,51,45],
     'point':[80,70,90,60]}

df1 = pd.DataFrame(d)
print(df1,type(df1))
print(df1.index)
print(df1.columns)
print(df1.values)

df1.index = ['학생1','학생2','학생3','학생4']
df1.index.name = ['학생이름']
df1.columns.name = ['정보']
print(df1)
print(df1.index)
print(df1.columns)

########################################
e = [['Jane',34,80],
     ['Tom',27,70],
     ['Alice',51,90],
     ['John',45,60]]
print(e)
df2 = pd.DataFrame(e,columns=['이름','나이','점수'],
                   index=['학생1','학생2','학생3','학생4'])
print(df2)

########################################