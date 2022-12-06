import matplotlib.pyplot as plt
import numpy as np 

def parebola_plotter(a=1, b=1, c=0, title='parebola_plotter'):
    x = np.arange(-10, 10, 2)
    y = a*x**2 + b*x + c
    plt.plot(x, y, label='my parabola')
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('title')
    plt.legend()
    plt.savefig('pic_3.png')

parebola_plotter()