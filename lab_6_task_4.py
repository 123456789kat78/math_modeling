#1
'''import matplotlib.pyplot as plt
import numpy as np 

def log.spiral_plotter(b=0.1):

    f = np.arange(0, 24, 0.1)
    r = np.e ** (b * f)
    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='spiral_plotter')
    plt.legend()
    plt.savefig('pic_9.png')

log.spiral_plotter()'''


#2
'''import matplotlib.pyplot as plt
import numpy as np 

def arx.spiral_plotter(k=0.1):

    f = np.arange(0, 24, 0.1)
    r = k * f 
    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='spiral_plotter')
    plt.legend()
    plt.savefig('pic_10.png')

arx.spiral_plotter()'''


#3
'''import matplotlib.pyplot as plt
import numpy as np 

def ges.spiral_plotter(k):

    f = np.arange(0,8 * np.pi, 0.1)
    r = k / np.sqrt(f) 
    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='spiral_plotter')
    plt.legend()
    plt.savefig('pic_11.png')

ges.spiral_plotter(0.2)'''

#4
import matplotlib.pyplot as plt
import numpy as np 

def roza_spiral_plotter(k):
    f = np.arange(0.2, 6, 0.1)
    r = np.sin(k * f)
    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='roza_spiral_plotter')
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.legend()
    plt.savefig('pic_12.png')

roza_spiral_plotter(5)









