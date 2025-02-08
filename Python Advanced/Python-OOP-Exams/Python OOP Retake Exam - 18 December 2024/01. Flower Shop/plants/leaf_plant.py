from project.plants.base_plant import BasePlant
from project.utils.validation import Validation


class LeafPlant(BasePlant):
    VALID_SIZE = ["S", "M", "L"]

    def __init__(self, name: str, price: float, water_needed: int, size: str):
        super().__init__(name, price, water_needed)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value: float):
        Validation.valid_collection(
            value, LeafPlant.VALID_SIZE, "Size must be a valid one!")
        self.__size = value
        
    def plant_details(self):
        return f"Leaf Plant: {self.name}, Price: {self.price:.2f}, Watering: {self.water_needed}ml, Size: {self.size}"


