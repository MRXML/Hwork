from random import randint as r
x = [r(1, 9) for n in range(4)]
y = x + [num * 2 for num in x]
print(x)
print(y)