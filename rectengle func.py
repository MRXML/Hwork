def rectangle(x, y):
    r = ''
    for i in range(x):
        if i == 0 or i == x - 1:
            r += "*" * y + '*\n'
        else:
            r += "*" + ' ' * (y - 1) + '*\n'
    return r
w, h = int(input('enter x cor')), int(input('enter y cor'))
print(rectangle(w, h))