import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 60, 1)

def mat_function(s, t):
    d = g - (y / m  * v **2)
    return d

g = 10
m = 100
v = 20
y = 0.300

d_t = odeint(mat_function, v, t)

plt.plot(t, d_t[:, 0],label='движение')
plt.xlabel('Сопротивление')
plt.ylabel('Сила')
plt.title('Cилааааа')
plt.legend()
 
plt.savefig('mat_tozka.png')

