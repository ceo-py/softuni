from project.appliances.appliance import Appliance


class TV(Appliance):
    default_cost = 1.5

    def __init__(self):
        super().__init__(self.default_cost)
