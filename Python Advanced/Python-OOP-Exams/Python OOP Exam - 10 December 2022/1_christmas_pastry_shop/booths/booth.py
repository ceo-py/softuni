from abc import ABC, abstractmethod

from project.validation.validation import Validation


class Booth(ABC):

    def __init__(self, booth_number: int,  capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validation.number_is_less_than_0(value, "Capacity cannot be a negative number!")
        self.__capacity = value

    def leave_booth(self):
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    def calculate_bill(self):
        return sum([d.price for d in self.delicacy_orders]) + self.price_for_reservation

    @abstractmethod
    def reserve(self, number_of_people: int):
        ...