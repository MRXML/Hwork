t = input('')
c = {}
for i in t.split():
    if i not in c:
        c[i] = t.count(i)
print(c)