import logging

logger = logging.getLogger('order')
logger.setLevel(logging.DEBUG)

file_hand = logging.FileHandler('log')
file_hand.setLevel(logging.INFO)

console_hand = logging.StreamHandler()
console_hand.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_hand.setFormatter(formatter)
console_hand.setFormatter(formatter)

logger.addHandler(file_hand)
logger.addHandler(console_hand)

class Dish:
    def __init__(self, name: str, description: str, price: float | int):
        self.name = name
        self.description = description
        self.price = price


    def descript(self):
        logger.info(f'{self.name}: {self.description}; {self.price}')



    def __str__(self):
        return f'{self.name} x {self.price}'


class Category:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)

    def __str__(self):
        return f'{self.name}\n' + '\n'.join(map(str, self.dishes))

class Menu:
    def __init__(self):
        self.categories = []

    def add_category(self, category: Category):
        self.categories.append(category)

    def __str__(self):
        return '\n'.join(map(str, self.categories))


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


class Order:
    def __init__(self):
        self.__dishes = []
        self.__quantities = []
        self.summa = 0
    def add_dish(self, dish: Dish, quantity=1):
        if not isinstance(dish, Dish):
            raise TypeError('Error in Dish datatype')
        if not isinstance(quantity, int | float):
            raise TypeError('Error in quantity of dishes')
        if quantity <= 0:
            raise ValueError('Quantity must be > 0. But less or equal got')
        self.__dishes.append(dish)
        self.__quantities.append(quantity)

    def total(self, discount: Discount):
        for item, quantity in zip(self.__dishes, self.__quantities):
            self.summa += item.price * quantity
        return self.summa * discount.discount()

dish1 = Dish('cheesecake1', 'description 1', 100)
dish2 = Dish('cheesecake2', 'description 2', 101)
dish3 = Dish('cheesecake3', 'description 3', 102)
dish4 = Dish('cheesecake4', 'description 4', 103)
dish5 = Dish('cheesecake5', 'description 5', 104)

dish1.descript()
dish2.descript()
dish3.descript()
dish4.descript()
dish5.descript()

cat1 = Category('category1')
cat2 = Category('category2')

cat1.add_dish(dish1)
cat1.add_dish(dish2)
cat1.add_dish(dish3)

cat2.add_dish(dish4)
cat2.add_dish(dish5)

menu = Menu()
menu.add_category(cat1)
menu.add_category(cat2)

print(menu)

order = Order()
order.add_dish(dish4)
print(order.total(GoldDiscount()))
