class Validation:

    @staticmethod
    def empty_string_or_white_space(text: str, message: str):
        if len(text) == 0 or text.isspace():
            raise ValueError(message)

    @staticmethod
    def check_number_less_than(number: float, number_to_be_less: float, message: str):
        if number < number_to_be_less:
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
    def check_if_string_is_two_characters_long(text: str, message: str):
        if len(text) < 2:
            raise ValueError(message)

    @staticmethod
    def check_for_duplicity(search_for: str, objects: list, attrib_check: str, message: str):
        if any(getattr(i, attrib_check) == search_for for i in objects):
            raise Exception(message)

    @staticmethod
    def check_if_object_with_given_name_exists(name: str, message: str):
        if name is None:
            raise Exception(message)

    @staticmethod
    def check_band_one_of_each_type_musician(message: str):
        raise Exception(message)

    @staticmethod
    def check_band_members_have_the_skills(members: list, all_members: list, message: str):
        if len(members) != len(all_members):
            raise Exception(message)






