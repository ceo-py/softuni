class Validation:

    @staticmethod
    def empty_or_white_space(text: str, error_message: str):
        if text.strip() == '':
            raise ValueError(error_message)

    @staticmethod
    def number_is_less_than(number: float, number_limit: float, error_message: str):
        if number <= number_limit:
            raise ValueError(error_message)

    @staticmethod
    def symbols_are_long(symbols: str, symbols_limit: float, error_message: str):
        if len(symbols) != symbols_limit:
            raise ValueError(error_message)

    @staticmethod
    def is_type_correct(type: str, correct_type: dict, error_message: str):
        if type not in correct_type:
            raise Exception(error_message)

    @staticmethod
    def cant_be_granted(error_message: str):
        raise Exception(error_message)

    @staticmethod
    def has_loan(error_message: str):
        raise Exception(error_message)
