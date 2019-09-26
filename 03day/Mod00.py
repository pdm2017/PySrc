# Mod00.py
print('name: {0}'.format(__name__))
import Calc00
import Calc00 as c
from Calc00 import *

x = 20; y = 10
Calc00.Sum(x,y)
c.Sub(x,y)
Mul(x,y)

import sys
for path in sys.path: print(path)
