class Validation:

    @staticmethod
    def name_empty_str(name: str):
        if len(name) == 0:
            raise ValueError("Name cannot be an empty string.")

    @staticmethod
    def energy_negative_number(num: int):
        if num < 0:
            raise ValueError("Energy cannot be less than zero.")

    @staticmethod
    def player_name_empty_str(name: str):
        if len(name) == 0:
            raise ValueError("Name not valid!")

    @staticmethod
    def player_name_duplicate(name: str, name_list):
        if name in name_list:
            raise ValueError(f"Name {name} is already used!")

    @staticmethod
    def player_age_restriction(num: int):
        if num < 12:
            raise ValueError("The player cannot be under 12 years old!")

    @staticmethod
    def player_max_stamina(num: int):
        if num < 0 or num > 100:
            raise ValueError("Stamina not valid!")

    @staticmethod
    def player_no_food_left(type_food: str, list_food: list):
        if all(type_food != h.__class__.__name__ for h in list_food):
            raise ValueError("There are no food supplies left!")

    @staticmethod
    def player_no_drink_left(type_drink: str, list_drink: list):
        if all(type_drink != h.__class__.__name__ for h in list_drink):
            raise ValueError("There are no drink supplies left!")
