from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def drive(self, kilometers):
        if kilometers * SportCar.DEFAULT_FUEL_CONSUMPTION <= self.fuel:
            self.fuel -= kilometers * SportCar.DEFAULT_FUEL_CONSUMPTION