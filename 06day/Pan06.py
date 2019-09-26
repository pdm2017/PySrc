# Pan06.py

import pandas as pd

df1 = pd.read_csv('./data/01. CCTV_in_Seoul.csv',encoding='utf-8')
print(df1)

print(df1.describe())

print(df1.head())
print(df1.tail(3))

print(df1.columns)
print(df1.columns[0])

df1.rename(columns={df1.columns[0]:'구 이름'},inplace=True)
print(df1.head())