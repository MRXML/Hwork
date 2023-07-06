c = {}
while True:
    a = int(input('1 new contact 2 ssearch contact 3 delete contact \n'))
    if a == 1:
        n, f = input('enter name'), input('enter phone number')
        c[n] = f
    elif a == 2:
        n = input('enter name')
        print(c.get(n))
    elif a == 3:
        n = input('enter name')
        del c[n]
    i = str(input('continue?'))
    if i.lower() == 'no':
        break