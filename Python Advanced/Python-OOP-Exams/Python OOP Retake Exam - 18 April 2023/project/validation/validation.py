class Validation:

    @staticmethod
    def empty_or_white_space(text: str, error_message: str):
        if text.strip() == '':
            raise ValueError(error_message)

    @staticmethod
    def number_is_less_than(number: float, number_limit: float, error_message: str):
        if number < number_limit:
            raise ValueError(error_message)