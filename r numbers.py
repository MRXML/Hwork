def r(y):
    n = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    d = 0
    p = 0
    for char in reversed(y):
        v = n[char]
        if v >= p:
            d += v
        else:
            d -= v
        p = v
    return d

x = str(input('').upper())
print(r(x))
