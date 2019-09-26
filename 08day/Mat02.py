# Mat02.py
import matplotlib.pyplot as plt
a = [10,20,30,40,50]
b = range(0,100)
c = [1,2,3,4,5]
d = range(0,11)
e = [i**2 for i in d]
f = [i+10 for i in d]

plt.plot(d,e,'gs')
plt.plot(d,f,'ro')
plt.show()