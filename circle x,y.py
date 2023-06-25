import math
x, y = int(input('enter x')), int(input('enter y'))
print('it is in circle' if math.sqrt(x ** 2 + y ** 2) <= 4 else 'it is not in circle')