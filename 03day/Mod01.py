# Mod01.py
# <-- /MyCalc01 / Calc01.py
print('name: {0}'.format(__name__))
from MyCalc01 import Calc01
from MyCalc01 import Calc01 as c
from MyCalc01.Calc01 import *
import MyCalc01.Calc01
x = 200; y = 100;
Calc01.Sum(x,y)
c.Sub(x,y)
Mul(x,y)