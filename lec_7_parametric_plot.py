
'''f(x(t), y(t))=0
#t - некоторый параметр / переменная величина
#() - параметрическое задание'''

import matplotlib.pyplot as plt
import numpy as np
R = 3

alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)#параметр

x = R * np.cos(alpha)
y = R * np.sin(alpha)


plt.plot(x, y, ls='--', lw=3)
#ls - пунктир 
#lw - сплошная линия

plt.axis('equal')

plt.savefig('kz.png')