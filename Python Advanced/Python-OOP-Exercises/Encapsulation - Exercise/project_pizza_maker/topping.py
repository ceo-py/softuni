from project.validation.validation import Validation


class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value):
        Validation.empty_string(value, "The topping type cannot be an empty string")
        self.__topping_type = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        Validation.number_less_than_to(value, 0, "The weight cannot be less or equal to zero")
        self.__weight = value

