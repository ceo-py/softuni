from project.validation.validation import Validation


class Player:
    name_set = set()

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.player_name_empty_str(value)
        Validation.player_name_duplicate(value, self.name_set)
        self.name_set.add(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validation.player_age_restriction(value)
        self.__age = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validation.player_max_stamina(value)
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
