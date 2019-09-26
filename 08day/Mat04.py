# Mat04.py
# 선 그래프
import matplotlib.pyplot as plt
# plt.함수()

#data1 = [10,14,19,20,25]
#plt.plot(data1)

import numpy as np
x = np.arange(-4.5,5,0.5)
y = 2*x**2
print([x,y])
plt.plot(x,y)
plt.show()