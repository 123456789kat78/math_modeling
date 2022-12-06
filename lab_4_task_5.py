def area(*arg< **kw):
    if kw['figure'] == 'square':
        s = arg[0] ** 2
    elif kw['figure'] == 'rectangle':
        s = arg[0] * arg[1]
    else:
        s = 1 / 2 * arg[0] * arg[1]
        print(s)

area(2 , 5, 7,figure = 'triangle')