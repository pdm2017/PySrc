# Pan02.py
import numpy as np, pandas as pd

f = np.random.randn(4,3) ; print(f)
df3 = pd.DataFrame(f) ; print(df3)
df3 = pd.DataFrame(f,columns=['A','B','C']) ; print(df3)
df3 = pd.DataFrame(np.random.randn(4,3),columns=['가','나','다']) ;
print(df3)

g = {'name':['Jane','Tom','Alice','John'],
     'age':[34,27,51,45],
     'point':[80,70,90,60]}
print(g)
df4 = pd.DataFrame(g); print(df4)

df4 = pd.DataFrame(g,columns=['name','point','age','etc'],
                   index=['학생1','학생2','학생3','학생4'])

print(df4) # NaN : Not a Number (Null)

df5 = pd.Series([1,2,3,np.nan,5,6])
print(df5)

a = [1,2,3,4,5]; print(sum(a))
#b = [1,2,3,None,4,5]; print(sum(b))
c = pd.Series([1,2,3,np.nan,5,6])
print(sum(c))