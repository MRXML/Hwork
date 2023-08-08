from category import *
class Menu:
    def __init__(self):
        self.categories = []

    def add_category(self, category: Category):
        self.categories.append(category)

    def __str__(self):
        return '\n'.join(map(str, self.categories))


