class Product:
    def __init__(self, name: str, price: int, about: str):
        self.name = name
        self.price = price
        self.about = about

    def __repr__(self):
        return f'{self.name}: {self.price}'

    def __str__(self):
        return f'{self.name}: {self.price}, {self.about}'


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(product.price for product in self.products)
product1 = Product('Mivina', 12, 'Instant Nodles')
product2 = Product('Jacobs', 5, 'Coffee')
cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
for product in cart.products:
    print(product)


print(f'Price: {cart.total_price()}')
