class Validation:

    @staticmethod
    def empty_string_or_white_space(text: str, message: str):
        if len(text) == 0 or text.isspace():
            raise ValueError(message)

    @staticmethod
    def number_under_16(number: int, message: str):
        if number < 16:
            raise ValueError(message)

    @staticmethod
    def check_if_item_is_in_items(item: str, items: iter, message: str):
        if item not in items:
            raise ValueError(message)

    @staticmethod
    def check_for_item_duplicity_in_iter(item: str, items: iter, message: str):
        if item in items:
            raise Exception(message)

    @staticmethod
    def check_for_empty_string(text: str, message: str):
        if len(text) == 0:
            raise ValueError(message)

    @staticmethod
    def check_number_less_than_one(number: float, message: str):
        if number < 1:
            raise ValueError(message)

    @staticmethod
    def check_if_number_is_negative(number: float, message: str):
        if number < 0:
            raise ValueError(message)

    @staticmethod
    def check_if_string_is_two_characters_long(text: str, message: str):
        if len(text) < 2:
            raise ValueError(message)

    @staticmethod
    def check_for_name_duplicity(name: str, names: list, message: str):
        if any(i.name == name for i in names):
            raise Exception(message)

    @staticmethod
    def check_for_concert_place_duplicity(place: str, places: list, message: str):
        if any(p.place == place for p in places):
            raise Exception(message)

    @staticmethod
    def check_if_object_with_given_name_exists(name: str, message: str):
        if name is None:
            raise Exception(message)

    @staticmethod
    def check_band_one_of_each_type_musician(members: list, message: str):
        if len(members) < 3:
            raise Exception(message)

    @staticmethod
    def check_band_members_have_the_skills(members: list, all_members: list, message: str):
        if len(members) != len(all_members):
            raise Exception(message)






