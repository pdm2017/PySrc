# Mat03.py

import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0,12,0.01)
b = np.sin(a)

plt.figure(figsize=(10,6))
plt.plot(a,b,'r')
plt.grid()
plt.xlabel('x line')
plt.ylabel('y line')
plt.title('Example of plt')
plt.show()
