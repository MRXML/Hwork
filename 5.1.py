n, n1, n2 = int(input("n=1")), int(input("n2=")), int(input("n3="))
print(n if n > n1 and n2 else n1 if n1 > n and n1 > n2 else n2)
