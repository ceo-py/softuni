class Validation:

    @staticmethod
    def empty_or_white_space(text: str, error_message: str):
        if text.strip() == '':
            raise ValueError(error_message)

    @staticmethod
    def less_than_or_equal_to(number: float, target_number: float, error_message: str):
        if number <= target_number:
            raise ValueError(error_message)

    @staticmethod
    def is_type_valid(type: str, correct_types: dict, error_message: str):
        if type not in correct_types:
            raise Exception(error_message)

    @staticmethod
    def can_be_add(limit: int, total_robots: int, error_message: str):
        if total_robots >= limit:
            raise Exception(error_message)

    @staticmethod
    def item_exist(name: str, collection: list, error_message):
        for i in collection:
            if i.name == name:
                return

        raise Exception(error_message)