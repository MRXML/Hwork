from random import randint as r

def line(l, t):
    for i in range(len(l)):
        if l[i] == t:
            return i
    return -1
m = [r(1, 10) for i in range(r(10, 15))]
c = input('enter number')
print(line(m, int(c)))
print(f'list was: {m}')