from project.drink.drink import Drink


class Water(Drink):
    costs = 1.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.costs, brand)
