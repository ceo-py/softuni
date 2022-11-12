from project.car.car import Car


class SportsCar(Car):
    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    @property
    def min_speed_limit(self):
        return 400

    @property
    def max_speed_limit(self):
        return 600
