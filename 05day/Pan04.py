# Pan04.py
import pandas as pd
a = {'name':['Jane','Tom','Alice','John'],
     'age':[34,27,51,45],
     'point':[80,70,90,60]}
print(a)
df1 = pd.DataFrame(a,columns=['name','point','age','etc'],
                   index=['학생1','학생2','학생3','학생4'])
print(df1)
############################################################
print(df1.loc['학생1'])
print(df1.loc['학생1',])
print(df1.loc['학생1',:])

# print(df1.loc[,])
print(df1.loc[:,:]) # 전체
print(df1.loc['학생1','name']) # loc : 인덱싱
print(df1.loc['학생1':'학생2','name':'point']) # loc : 슬라이싱
