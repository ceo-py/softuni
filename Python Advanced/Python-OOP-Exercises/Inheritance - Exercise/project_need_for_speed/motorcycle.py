from project.vehicle import Vehicle

class Motorcycle(Vehicle):
    def drive(self, kilometers):
        if kilometers * Motorcycle.DEFAULT_FUEL_CONSUMPTION <= self.fuel:
            self.fuel -= kilometers * Motorcycle.DEFAULT_FUEL_CONSUMPTION
