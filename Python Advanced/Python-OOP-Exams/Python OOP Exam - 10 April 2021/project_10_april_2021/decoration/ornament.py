from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    set_comfort = 1
    set_price = 5

    def __init__(self):
        super().__init__(self.set_comfort, self.set_price)


