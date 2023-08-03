class Fraction:
    def __init__(self, x: int, y: int):
        self.numerator = x
        self.denominator = y

    def __eq__(self, other):
        if isinstance(other, Fraction):
            if self.denominator <= other.denominator:
                if self.numerator > other.numerator:
                    return f'{self.numerator}/{self.denominator} is bigger'
                elif self.denominator > other.denominator:
                    return f'{other.numerator}/{other.denominator} is bigger'
            elif self.numerator == other.denominator:
                if self.denominator < other.denominator:
                    return f'{self.numerator}/{self.denominator} is bigger'
                else:
                    return f'{other.numerator}/{other.denominator} is bigger'


    def __add__(self, other):
        if isinstance(other, Fraction):
            return f'{self.numerator + other.numerator}/{self.denominator}'

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return f'{self.numerator - other.numerator}/{self.denominator}'

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return f'{self.numerator * other.numerator}/{self.denominator * self.denominator}'

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return f'{self.numerator * other.denominator}/{self.denominator * other.numerator}'

    def __str__(self):
        return f"summ: {c + b}, subtraction: {c - b}, multiplication: {c * b}, division {c / b}, {c == b} \n"\
               f'summ: {f + m}, subtraction: {f - m}, multiplication: {f * m}, division {f / m}'

c = Fraction(2, 3)
b = Fraction(12, 3)
f = Fraction(2, 3)
m = Fraction(4, 3)
print(Fraction(c, b))