import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 20, 0.1)
def difirins_function(i, t):
    d = - k * i * t 
    return d

k = 0.08
i0 = 1000

i_0 = odeint(difirins_function, i0, t)

plt.plot(t, i_0[:, 0],label='инвестиции')
plt.xlabel('Кол-во лет')
plt.ylabel('инвестиции')
plt.title('вклад')
plt.legend()
 
plt.savefig('investizii.png')
