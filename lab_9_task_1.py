import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(0, 60, 1)
def bakteria_function(s, t):
    pip = k * s
    return pip

s_0 = 10
k = 1/15

s_t = odeint(bakteria_function, s_0, t)
 
plt.plot(t, s_t[:, 0],label='бяки')
plt.xlabel('Время размножения')
plt.ylabel('Количество размножения')
plt.title('скорость размножения бактерий')
plt.legend()
 
plt.savefig('bakteria.png')

