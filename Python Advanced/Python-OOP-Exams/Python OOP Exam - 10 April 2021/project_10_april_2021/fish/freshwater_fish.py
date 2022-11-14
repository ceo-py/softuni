from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.__initial_size, price)

    @property
    def __add_size(self):
        return 3

    @property
    def __initial_size(self):
        return 3

    def eat(self):
        self.size += self.__add_size
