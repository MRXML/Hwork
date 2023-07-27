class Invalid_price(Exception):
    def __init__(self, price):
        super().__init__()
        self.price = price

    def __str__(self):
        return f'Price cannot be less than or equal to zero. (Price = {self.price})'


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.check()

    def check(self):
        if self.price <= 0:
            raise Invalid_price(self.price)

    def __str__(self):
        return f'{self.name}: {self.price:.2f} UAH'


class Cart:
    def __init__(self):
        self.__products = []
        self.__quantities = []

    def add_product(self, product: Product, quantity=1):
        if not isinstance(product, Product):
            raise TypeError('Error in Product datatype')
        if not isinstance(quantity, (int, float)):
            raise TypeError('Error in quantity of Product')
        if quantity <= 0:
            raise ValueError('Quantity must be greater than 0.')
        self.__products.append(product)
        self.__quantities.append(quantity)

    def total(self):
        summa = 0
        for item, quantity in zip(self.__products, self.__quantities):
            summa += item.price * quantity
        return summa

    def __str__(self):
        res = ''
        for item, quantity in zip(self.__products, self.__quantities):
            res += f'{item} x {quantity} = {item.price * quantity:.2f} UAH\n'

        res += f'Total = {self.total():.2f} UAH'
        return res


if __name__ == '__main__':
    try:
        pr1 = Product('apple', 0)
        pr2 = Product('apple lux', 40)
        pr3 = Product('banana', 20)
        pr4 = Product('orange', 10)

        cart = Cart()
        cart.add_product(pr1, 2)
        cart.add_product(pr4)
        cart.add_product(pr3, 3)

        print(cart)
    except Invalid_price as e:
        print(f'Invalid Price Error: {e}')
    except TypeError as e:
        print(f'Type Error: {e}')
    except ValueError as e:
        print(f'Value Error: {e}')
