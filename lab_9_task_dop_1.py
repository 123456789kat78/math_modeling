import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


R = 6400000
h = 50 * R 
r = np.arange(h +R, R, -1000)

def move_meteorit(v, r):
    dvdr = - G * M / (v * r ** 2)
    return dvdr

G = 6.67 * 20 ** (-11)
M = 6 * 10 ** 24 
v0 = 1

v_r = odeint(move_meteorit, v0, r)

plt.plot(r, v_r[:,  0],  label = 'траектория')
plt.xlabel('время')
plt.ylabel('')
plt.title('')
plt.legend()
 
plt.savefig('meteorit.png')
