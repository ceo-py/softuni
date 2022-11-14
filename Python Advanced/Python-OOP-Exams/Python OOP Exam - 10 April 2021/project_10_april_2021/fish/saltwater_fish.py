from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.__initial_size, price)

    @property
    def __add_size(self):
        return 2

    @property
    def __initial_size(self):
        return 5

    def eat(self):
        self.size += self.__add_size
