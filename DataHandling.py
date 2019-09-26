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

#------------------------------------------------------------
# 문자열로 되어 있는 컬럼을 Pandas의 DateTime 형으로 변환한다
#------------------------------------------------------------
data['DATETIME'] = pd.to_datetime(data['DATA2'], format = '%y-%m-%d %H:%M')
data['YEAR'] = pd.DatetimeIndex(data['DATETIME']).year
data['MONTH'] = pd.DatetimeIndex(data['DATETIME']).month
data['DATE'] = pd.DatetimeIndex(data['DATETIME']).day
data['DAY'] = pd.DatetimeIndex(data['DATETIME']).dayofweek
data['HOUR'] = pd.DatetimeIndex(data['DATETIME']).hour
data['MINUTE'] = pd.DatetimeIndex(data['DATETIME']).minute

# Pandas의 DataTime 형을 숫자로 변환한다
data['DATE_NUM'] = pd.to_numeric(data['DATETIME'], downcast='integer')

# 해당 컬럼에서 최소한의 값을 찾는다
_min_ = data['DATE_NUM'].min()

# 가장 최소값으로 빼주고 분단위 이므로 60 초를 나눠서 1분단위로 증가 시켜준다
data['DATE_SORT'] = (data['DATE_NUM'] - _min_) / (1000000000 * 60)
