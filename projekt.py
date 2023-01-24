from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np

x = []
y = []
colors = []
fig = plt.figure(figsize=(7,5))

def animation_func(i):
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))
    colors.append(np.random.rand(1))
    area = random.randint(0,30) * random.randint(0,30)
plt.xlim(0,100)
plt.ylim(0,100)

star, = plt.plot([], [], 'o', color='b') 

ani = FuncAnimation(fig, animation_func,interval = 100)

ani.save('7.3111.gif')
