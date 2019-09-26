# Pan03.py
import pandas as pd
a = {'name':['Jane','Tom','Alice','John'],
     'age':[34,27,51,45],
     'point':[80,70,90,60]}
print(a)
df1 = pd.DataFrame(a,columns=['name','point','age','etc'],
                   index=['학생1','학생2','학생3','학생4'])
print(df1)
print(df1['name'])
print(df1.name)
print(df1[['age','point']]) # 열 이름 호출
print(df1[1:3]) # 행 번호 호출 [숫자:숫자]
print(df1[1:2][['age','point']])
print(df1[1:2][['age']])
print(df1[1:2]['age'])
print(df1.loc['학생2']) # 행 이름 추출
print(df1.loc['학생2'][['age','point']]) # 행 이름, 열 이름 추출
print(df1.iloc[0]) # 행 번호 추출
print(df1['학생2':'학생3'])
print(df1.loc['학생2':'학생3'])

print(df1.loc['학생1','point'])
print(df1.loc['학생2':'학생3','point'])
print(df1.loc['학생2':'학생3','point':'age'])
print(df1.loc[:,'point':'age'])

