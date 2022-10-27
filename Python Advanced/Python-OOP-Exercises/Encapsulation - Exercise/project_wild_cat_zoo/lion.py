from project.animal import Animal


class Lion(Animal):
    def __init__(self, name: str, gender: str, age: int, money_for_care=0):
        super().__init__(name, gender, age, money_for_care)
        self.money_for_care = 50
