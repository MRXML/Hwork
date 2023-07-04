w, h = int(input("enter width")), \
       int(input("enter high"))
for i in range(w):
    print("*" * w)if i == 0 or i == h - 1 else print("*" + ' ' * (w - 2) + '*')