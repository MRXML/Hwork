a, b, c = int(input("enter side a")), \
                         int(input("enter side b")), \
                         int(input("enter side c"))
print("it is a triangle") if a + b > c and b + c > a and a + c > b else print("it is not a triangle")
