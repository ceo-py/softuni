from project.appliances.appliance import Appliance


class Fridge(Appliance):
    default_cost = 1.2

    def __init__(self):
        super().__init__(self.default_cost)
