from dish import *
from discount import *
class Order:
    def __init__(self):
        self.__dishes = []
        self.__quantities = []

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
        summa = 0
        for item, quantity in zip(self.__dishes, self.__quantities):
            summa += item.price * quantity
        return summa * discount.discount()
