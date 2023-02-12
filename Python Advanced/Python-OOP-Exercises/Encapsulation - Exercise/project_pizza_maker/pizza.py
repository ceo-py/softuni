from project.dough import Dough
from project.topping import Topping
from project.validation.validation import Validation


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.empty_string(value, "The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        Validation.check_if_its_none(value, "You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        Validation.number_less_than_to(value, 0, "The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value



    def add_topping(self, topping: Topping):
        Validation.number_less_than_to(self.max_number_of_toppings, len(self.toppings), "Not enough space for another topping")
        self.toppings[topping.topping_type] = self.toppings.get(topping.topping_type, 0) +  topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())