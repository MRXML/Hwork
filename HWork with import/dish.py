class Dish:
    def __init__(self, name: str, description: str, price: float | int):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name} x {self.price}'
