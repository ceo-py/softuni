from abc import ABC, abstractmethod

from project.validation.validation import Validation


class BaseVehicle(ABC):
    BATTERY_INITIAL_CHARGE = 100

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level = 100
        self.is_damaged = False

    @abstractmethod
    def drive(self, mileage: float):
        pass

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        Validation.empty_or_white_space(value, 'Brand cannot be empty!')
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validation.empty_or_white_space(value, 'Model cannot be empty!')
        self.__model = value

    @property
    def license_plate_number(self):
        return self.__license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value):
        Validation.empty_or_white_space(value, 'License plate number is required!')
        self.__license_plate_number = value

    def recharge(self):
        self.battery_level = BaseVehicle.BATTERY_INITIAL_CHARGE

    def change_status(self):
        self.is_damaged = not self.is_damaged

    def __str__(self):
        output = f'{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% Status: '
        if self.is_damaged:
            output += 'Damaged'
        else: output += 'OK'
        return output