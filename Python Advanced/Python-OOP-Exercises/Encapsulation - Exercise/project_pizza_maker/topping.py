class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value):
        if value == "":
            raise ValueError("The topping type cannot be an empty string")
        self.__topping_type = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = value


'''
topping_type: str - if the topping is an empty string, raise a 
ValueError with the message "The topping type cannot be an empty string"
weight: float - if the weight is 0 or less, raise a ValueError with the message 
"The weight cannot be less or equal to zero"

'''