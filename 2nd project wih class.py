class Dish:
    def __init__(self, name, about, price):
        self.name = name
        self.about = about
        self.price = price

    def __str__(self):
        return f'dish: {self.name}, is in your order ({self.price})'
class MenuC:
    def __init__(self, name):
        self.dish = name
class Menu:
    def __init__(self, order, cat):
        self.cat = cat
class Ord:
    def __init__(self, name, price):
        self.order_price = int(price)
        self.dish = str(name)
        self.order_dish = ''
        self.i = 0

    def add(self):
        self.i += self.order_price
        self.order_dish += self.dish
        return f'your order: {self.order_dish}\nyou need to pay {self.i}'
def convert(order):
    a = {
        'pizza': f'Pizza pizza 12 bake',
        'soup': f'Soup good 10 water',
        'sushi': f'Sushi wih_fish 30 Asian_cuisine',
        'tee': f'Tee blue_tee 7 drinks',
        'coffee': f'Kopi_Ludvig_coffee coffee 100 drinks'
    }
    dish_i = a[order].split()
    dish_price = [s for s in dish_i if s.isdigit()]
    return dish_i[1], dish_i[2], dish_price[0]
order = input(f'Menu: Pizza, Soup, Sushi, Tee, Coffee.\nWhat do you want?').lower()
dish_n, dish_a, dish_p = convert(order)
dish_o = Dish(dish_n, dish_a, dish_p)
print(dish_o)
menu_cat = Menu(order, 'category_placeholder')
menu_c = MenuC(order)
order_o = Ord(dish_n, dish_p)
print(order_o.add())