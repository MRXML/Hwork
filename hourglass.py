n = int(input(""))

for i in range(n, 0, -2):
    print(' ' * ((n - i) // 2) + '*' * i)

for i in range(3, n + 1, 2):
    print(' ' * ((n - i) // 2) + '*' * i)

