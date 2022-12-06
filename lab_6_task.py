import matplotlib.pyplot as plt
import numpy as np 

x = np.array([1, 1, 5, 5, 1])
y = np.array([1, 5, 5, 1, 1])
plt.plot(x, y)
plt.savefig('pic_5.png')