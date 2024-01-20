from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float, weight: int = 9):
        super().__init__(name, kind, price, weight)

    @staticmethod
    def can_be_add(service_name: str):
        return service_name == 'MainService'

    def eating(self):
        self.weight += 3