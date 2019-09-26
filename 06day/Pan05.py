#!/usr/bin/env python
# coding: utf-8

# # 1. Jupyter NoteBook 시작

# In[1]:


print("Hello")


# In[2]:


"안녕하세요"


# In[4]:


import pandas as pd


# In[6]:


pd.__version__


# In[7]:


"SK하이닉스"


# In[8]:


a = {'name':['Jane','Tom','Alice','John'],
     'age':[34,27,51,45],
     'point':[80,70,90,60]}
df1 = pd.DataFrame(a,columns=['name','point','age','etc'],
                   index=['학생1','학생2','학생3','학생4'])


# In[9]:


df1


# In[14]:


df1.loc['학생1':'학생2']


# In[16]:


df1.loc['학생1':'학생2','name':'age']


# In[18]:


df1.iloc[0:1]


# In[19]:


df1.iloc[0:1,0:2]


# In[20]:


df1


# In[24]:


df1.loc['학생1','etc'] = 1


# In[29]:


df1.loc[:,'etc'] = 2


# In[30]:


df1


# In[34]:


df1.loc['학생5',:] = ['Sophia', 100, 9,3];
df1.loc['학생6',:] = ['James', 77, 21, 4]


# In[35]:


df1


# In[38]:


df1['point']>=75


# In[39]:


df1[df1['point']>=75]


# In[45]:


df1[df1['point']>=75]


# In[46]:


import numpy as np


# In[47]:


n1 = np.arange(1,21)


# In[48]:


n1


# In[49]:


n1>10


# In[50]:


n1[n1>10]


# In[51]:


df1


# In[53]:


df1[df1['age']>=30]


# In[55]:


df1.loc[df1['age']>=30,:]


# In[56]:


df1


# In[57]:


df1[(df1['point']>75)&(df1['age']>=30)]


# In[59]:


df1.loc[(df1['point']>75)&(df1['age']>=30),:]


# In[72]:


df1[(df1['point']>75)&(df1['age']>=30)][['name','age']]


# In[75]:


df1.loc[df1['age']>=30,['name','age']]


# In[80]:


df1.loc[df1['age']>=30,'name':'age']


# In[93]:


df1.loc[df1['point']<=70,'etc'] = 5


# In[97]:


df1


# In[98]:


df1['point'].mean()


# In[99]:


df1['point'].sum()


# In[100]:


df1['point'].var()


# In[101]:


df1['point'].std()


# In[102]:


df1.describe()


# In[ ]:




