class Discount:
    def __init__(self, value=0):
        self.value = value

    def discount(self):
        raise NotImplementedError


class RegularDiscount(Discount):
    def __init__(self, value=5):
        super().__init__(value)

    def discount(self):
        return 1 - self.value / 100


class SilverDiscount(Discount):
    def __init__(self, value=10):
        super().__init__(value)

    def discount(self):
        return 1 - self.value / 100


class GoldDiscount(Discount):
    def __init__(self, value=20):
        super().__init__(value)

    def discount(self):
        return 1 - self.value / 100
