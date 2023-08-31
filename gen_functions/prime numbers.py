def prime(last: int = 20):
    count, value = 0, 2
    while count < last:
        is_p = True
        for i in range(2, value):
            if value % i == 0:
                is_p = False
                break
            if is_p:
                yield value
                count += 1
            value += 1
for n in prime(20):
    print(n)