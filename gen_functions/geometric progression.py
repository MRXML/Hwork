def geom_prog(a, b):
    c = 1
    for i in range(50):
        yield a
        a *= b
        c += 1

a, b = 2, 3
gen = geom_prog(a, b)
for _ in range(10):
    print(next(gen))