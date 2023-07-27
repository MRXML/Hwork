class Discount:
    def __init__(self, card, price):
        self.card = card
        self.cost = price

    def calculate_discount(self):
        if self.card == 'REGULAR':
            return self.cost * 0.95
        elif self.card == 'SILVER':
            return self.cost * 0.9
        elif self.card == 'GOLD':
            return self.cost * 0.8
        else:
            print('Invalid card type.')
            return None

class Regular(Discount):
    def __init__(self, card, cost, rcost):
        super().__init__(card, cost)
        self.rcost = rcost

    def calculate_discount(self):
        self.rcost -= self.cost * (self.card / 100)

class Silver(Discount):
    def __init__(self, card, cost, scost):
        super().__init__(card, cost)
        self.scost = scost

    def calculate_discount(self):
        self.scost -= self.cost * (self.card / 100)

class Gold(Discount):
    def __init__(self, card, cost, gcost):
        super().__init__(card, cost)
        self.gcost = gcost

    def calculate_discount(self):
        self.gcost -= self.cost * (self.card / 100)

class Total(Regular, Silver, Gold):
    def __init__(self, card, cost):
        super().__init__(card, cost, cost)

    def __str__(self):
        if self.card == 'REGULAR':
            return f'now price = {self.rcost}, you used {self.card} card'
        elif self.card == 'SILVER':
            return f'now price = {self.scost}, you used {self.card} card'
        elif self.card == 'GOLD':
            return f'now price = {self.gcost}, you used {self.card} card'
        else:
            return 'error'

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
    def __init__(self, name, price, cost):
        self.order_price = int(price)
        self.dish = str(name)
        self.order_dish = cost
        self.i = int(cost)

    def add(self):
        self.i += self.order_price
        self.order_dish += " " + self.dish
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
    return dish_i[1], dish_i[2], int(dish_price[0])

order = input(f'Menu: Pizza, Soup, Sushi, Tee, Coffee.\nWhat do you want?').lower()
dish_n, dish_a, dish_p = convert(order)
dish_o = Dish(dish_n, dish_a, dish_p)
print(dish_o)

order_o = Ord(dish_n, dish_p, dish_p)
print(order_o.add())

disc = str(input(f'if you have a discount card enter class of card')).upper()

if disc in ['REGULAR', 'SILVER', 'GOLD']:
    total = Total(disc, int(dish_p))
    total.calculate_discount()
    print(total)
else:
    print('error')
