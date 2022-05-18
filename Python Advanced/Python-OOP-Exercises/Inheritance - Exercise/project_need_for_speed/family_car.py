from project.car import Car


class FamilyCar(Car):

    def drive(self, kilometers):
        if kilometers * FamilyCar.DEFAULT_FUEL_CONSUMPTION <= self.fuel:
            self.fuel -= kilometers * FamilyCar.DEFAULT_FUEL_CONSUMPTION