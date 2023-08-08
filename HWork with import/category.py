from dish import *
class Category:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)

    def __str__(self):
        return f'{self.name}\n' + '\n'.join(map(str, self.dishes))
