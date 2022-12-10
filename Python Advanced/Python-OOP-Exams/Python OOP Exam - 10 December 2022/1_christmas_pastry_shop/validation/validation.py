class Validation:

    @staticmethod
    def text_empty_string_or_white_space(text: str, message: str):
        if text == "" or text.isspace():
            raise ValueError(message)

    @staticmethod
    def number_is_less_than_or_equal_0(number: float, message: str):
        if number <= 0:
            raise ValueError(message)

    @staticmethod
    def number_is_less_than_0(number: float, message: str):
        if number < 0:
            raise ValueError(message)

    @staticmethod
    def item_duplicity(delicacy_name: str, list_with_delicacy: object, message: str):
        if any(delicacy_name == d.name for d in list_with_delicacy):
            raise Exception(message)

    @staticmethod
    def correct_type(type_: str, correct_types_: dict, message: str):
        if type_ not in correct_types_:
            raise Exception(message)

    @staticmethod
    def number_duplicity(booth_number: str, list_with_booth: object, message: str):
        if any(booth_number == b.booth_number for b in list_with_booth):
            raise Exception(message)

    @staticmethod
    def item_not_found(item: object, message: str):
        if not item:
            raise Exception(message)

