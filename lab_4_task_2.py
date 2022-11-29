import numpy as np
a = [1, 2 , 3, 4, 5, 6, 7, 8 , 9, 10 ]
def my_func(k):
    count = 0 
    s = 1
    for i in k:
        s = s * i
        count = count * 1
    print(s)

my_func(a)
