s = str(input('').lstrip().rsplit())
def count (x):
    a = 0
    for i in x:
        if i == ' ':
            a += 1
        else:
            a += 0
    return a + 1
print(count(s))