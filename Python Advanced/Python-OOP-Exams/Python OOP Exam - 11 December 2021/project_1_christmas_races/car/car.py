from abc import ABC, abstractmethod

from project.validation.validation import Validation


class Car(ABC):
    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validation.car_model(value)
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        Validation.car_speed_limit(value, self.min_speed_limit, self.max_speed_limit)
        self.__speed_limit = value

