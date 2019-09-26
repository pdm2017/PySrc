import pandas as pd
import numpy as np

#----------------------------------------------
def replaceOutlierToLimit(s):
#----------------------------------------------
    '''
    입력 : Pandas.Series
    Series 형 (컬럼) 을 입력받으면, Outlier 값을 상한을 넘으면 상한으로, 하한을 넘으면 하한값으로 변환
    리턴 : Pandas.Series
    '''
    q1, q3 = s.quantile(q=[0.25, 0.75])
    iqr = q3 - q1    
    low_fense, hig_fense = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    tmpS = np.where(s < low_fense, low_fense, s)
    tmpS = np.where(tmpS > hig_fense, hig_fense, tmpS)
    return tmpS
