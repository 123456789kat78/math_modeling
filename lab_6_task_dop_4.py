import matplotlib.pyplot as plt
import numpy as np 

# x = [0, 1, 1, 2, 2]
# y = [10, 10, 9, 9, 8]

x = []
y = []

for i in range(10):
    x.append(i)
    y.append(10-i)

plt.plot(x, y, color='g', label='luchte', marker='>', ms=5) 

# --- Украшательства ---
plt.xlabel('Coord: x')
plt.ylabel('Coord: y')
plt.legend()
plt.title('Base')
plt.grid()
plt.savefig('pic_13.png')

