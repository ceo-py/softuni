from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00
    ADDITIONAL_CARGO_REDUCE = 5

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage = CargoVan.MAX_MILEAGE)

    def drive(self, mileage: float):
        self.battery_level -= (round(mileage / self.MAX_MILEAGE * 100) + self.ADDITIONAL_CARGO_REDUCE)
