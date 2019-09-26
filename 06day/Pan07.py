# Pan07.py

import pandas as pd

df1 = pd.read_excel('./data/01. population_in_Seoul.xls',encoding='utf-8')
print(df1)
print(df1.head())

df2 = pd.read_excel('./data/01. population_in_Seoul.xls',
                    header=2,
                    usecols='B,D,G,J,N',
                    encoding='utf-8')
print(df2)
print(df2.head())
print(df2.describe())