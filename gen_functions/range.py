def rang(start, stop, step=1):
    c = start
    while c < stop if step > 0 else c > stop:
        yield c
        c += step
