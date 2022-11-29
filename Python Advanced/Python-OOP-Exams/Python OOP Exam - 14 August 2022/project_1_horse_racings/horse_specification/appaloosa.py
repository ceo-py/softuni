from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    maximum_speed = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 2 > self.maximum_speed:
            self.speed = 120
        else:
            self.speed += 2
