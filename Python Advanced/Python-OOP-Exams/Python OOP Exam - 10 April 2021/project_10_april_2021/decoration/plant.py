from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    set_comfort = 5
    set_price = 10

    def __init__(self):
        super().__init__(self.set_comfort, self.set_price)


