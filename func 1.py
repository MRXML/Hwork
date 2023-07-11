def func(x, y, s):
    r = str(x + y) + s
    return r

n1, n2, st = int(input('enter n1')), \
             int(input('enter n2')), \
             input('enter string')
print(func(n1, n2, st))