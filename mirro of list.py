from random import randint as r
x = [r(1, 9) for n in range(r(1, 9))]
print(f"list:{x} mirror of the list: {x[::-1]}")