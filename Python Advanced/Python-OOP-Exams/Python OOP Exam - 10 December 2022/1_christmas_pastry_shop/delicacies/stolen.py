from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):

    def __init__(self, name: str, price: float, portion = 250):
        super().__init__(name, portion, price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
