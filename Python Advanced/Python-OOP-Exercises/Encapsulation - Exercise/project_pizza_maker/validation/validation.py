class Validation:

    @staticmethod
    def empty_string(string_: str, message: str):
        if len(string_) == 0:
            raise ValueError(message)

    @staticmethod
    def number_less_than_to(number: float, number_to_check: float, message: str):
        if number <= number_to_check:
            raise ValueError(message)

    @staticmethod
    def check_if_its_none(object_to_check: object, message: str):
        if object_to_check is None:
            raise ValueError(message)