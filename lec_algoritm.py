import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Пределы изменения переменной величины
# В данной задаче переменной величиной является время

t = np.arange(0, 10**6, 100)
def radio_function(m, t):
    dmdt = - k * m
    return dmdt

# Определение начальных условий и параметров
m_0 = 10
k = 1.61 * 10**(-6)

m_t = odeint(radio_function, m_0, t)
 
plt.plot(t, m_t[:, 0], label='Распад Висмута 210')

plt.xlabel('Период распада, секунды')
plt.ylabel('Функция распада')
plt.title('Радиоактивный распад')
plt.legend()
 
plt.savefig('algoritm.png')
