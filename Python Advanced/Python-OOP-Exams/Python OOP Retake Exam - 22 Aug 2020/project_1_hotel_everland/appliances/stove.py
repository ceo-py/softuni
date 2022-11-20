from project.appliances.appliance import Appliance


class Stove(Appliance):
    default_cost = 0.7

    def __init__(self):
        super().__init__(self.default_cost)
