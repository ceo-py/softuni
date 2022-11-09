from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    maximum_speed = 120
    train_gain = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
