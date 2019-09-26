# Mat01.py
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
print(x)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label='Sin')
plt.plot(x,y2,label='Cos',linestyle="--")
plt.xlabel("X")
plt.ylabel("Y")
plt.title(" Sin & Cos ")
plt.legend()
plt.show()
