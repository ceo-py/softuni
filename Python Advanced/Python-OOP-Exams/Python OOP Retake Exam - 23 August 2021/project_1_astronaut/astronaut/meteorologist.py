from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):

    def __init__(self, name: str, oxygen=90):
        super().__init__(name, oxygen)

    @property
    def breath_unit(self):
        return 15

    def breathe(self):
        self.oxygen -= self.breath_unit

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
