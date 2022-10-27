from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def drive(self, kilometers):
        if kilometers * Car.DEFAULT_FUEL_CONSUMPTION <= self.fuel:
            self.fuel -= kilometers * Car.DEFAULT_FUEL_CONSUMPTION
