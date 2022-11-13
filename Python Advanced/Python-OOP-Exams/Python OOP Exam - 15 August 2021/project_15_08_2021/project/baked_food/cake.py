from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    portion_size = 245

    def __init__(self, name: str, price: float):
        super().__init__(name, self.portion_size, price)
