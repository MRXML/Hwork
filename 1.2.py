n = int(input('enter nummer of the floor'))
an = n // 36
fn = (n - 1) % 36 // 4 + 1
nf = ((n - 1) % 36 % 4) + 1
print(an + 1)
print(fn)
print(nf)