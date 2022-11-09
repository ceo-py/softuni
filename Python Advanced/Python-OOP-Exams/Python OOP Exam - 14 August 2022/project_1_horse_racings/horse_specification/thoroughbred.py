from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    maximum_speed = 140
    train_gain = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
