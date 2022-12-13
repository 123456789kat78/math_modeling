import matplotlib.pyplot as plt
import numpy as np 

def ellips_plotter(a, b):

    x = np.arange(-3, 3, 0.1)
    y = np.arange(-3, 3, 0.1)
    X, Y = np.meshgrid(x, y)

    fxy = X**2 / a**2 + Y**2 / b**2 - 1
    
    plt.contour(X, Y, fxy)
    plt.savefig('pic_8.png')


ellips_plotter(2, 3)
