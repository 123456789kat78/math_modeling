

a = [1, 2 , 3, 4, 5, 6, 7, 8 , 9, 10 ]
def my_func(k):
    count = 0
    s = 0 
    for i in a:
        s = s + i
        count = count + 1
    t = s / count
    print(t)

my_func(a)