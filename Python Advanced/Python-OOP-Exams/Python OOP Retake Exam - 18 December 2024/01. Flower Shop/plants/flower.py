from project.plants.base_plant import BasePlant
from project.utils.validation import Validation


class Flower(BasePlant):
    VALID_SEASONS = ["Spring", "Summer", "Fall", "Winter"]

    def __init__(self, name: str, price: float, water_needed: int, blooming_season: str):
        super().__init__(name, price, water_needed)
        self.blooming_season = blooming_season

    @property
    def blooming_season(self):
        return self.__blooming_season

    @blooming_season.setter
    def blooming_season(self, value: str):
        Validation.valid_collection(
            value, Flower.VALID_SEASONS, "Blooming season must be a valid one!")
        self.__blooming_season = value
        
    def plant_details(self):
        return f"Flower: {self.name}, Price: {self.price:.2f}, Watering: {self.water_needed}ml, Blooming Season: {self.blooming_season}"


