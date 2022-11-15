import numpy as np
from random import randint

a = np.arange(5) * 0

for i in range(5):
  a[i] = randint(0, 100)
  
print(a)


s = 0 
for element in a:
  if element > s:
    s = element
print(s)