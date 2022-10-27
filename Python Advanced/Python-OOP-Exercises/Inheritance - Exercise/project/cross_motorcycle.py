from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    def drive(self, kilometers):
        if kilometers * Motorcycle.DEFAULT_FUEL_CONSUMPTION <= self.fuel:
            self.fuel -= kilometers * Motorcycle.DEFAULT_FUEL_CONSUMPTION