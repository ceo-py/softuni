from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    maximum_speed = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 3 > self.maximum_speed:
            self.speed = 140
        else:
            self.speed += 3
