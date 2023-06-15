def math():
    p = int(input("enter r"))
    r = int(input("enter n"))
    years = int(input("enter p"))
    res = p * (1 + r/100) ** years
    return res
print(math())