from menu import *
from order import *

dish1 = Dish('cheesecake1', 'description 1', 100)
dish2 = Dish('cheesecake2', 'description 2', 101)
dish3 = Dish('cheesecake3', 'description 3', 102)
dish4 = Dish('cheesecake4', 'description 4', 103)
dish5 = Dish('cheesecake5', 'description 5', 104)
dish6 = Dish('cheesecake6', 'description 6', 105)

cat1 = Category('category1')
cat2 = Category('category2')

cat1.add_dish(dish1)
cat1.add_dish(dish2)
cat1.add_dish(dish3)

cat2.add_dish(dish4)
cat2.add_dish(dish5)
cat2.add_dish(dish6)

menu = Menu()
menu.add_category(cat1)
menu.add_category(cat2)

print(menu)

order = Order()
order.add_dish(dish4)
order.add_dish(dish6, 2)
print(order.total(GoldDiscount()))