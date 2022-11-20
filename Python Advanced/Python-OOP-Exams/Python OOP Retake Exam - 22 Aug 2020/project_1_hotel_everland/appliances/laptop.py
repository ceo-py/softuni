from project.appliances.appliance import Appliance


class Laptop(Appliance):
    default_cost = 1.0

    def __init__(self):
        super().__init__(self.default_cost)
