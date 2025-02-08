class Validation:


    @staticmethod
    def is_number_in_range_of_two_numbers(number: int, down_limit: int, upper_limit: int, message: str) -> None:
        if down_limit > number or number > upper_limit:
            raise ValueError(message)

    @staticmethod
    def is_number_equal_or_under(number: float, limit: float, message: str) -> None:
        if number <= limit:
            raise ValueError(message)
        
    @staticmethod
    def empty_string_or_empty_spaces(text: str, message: str) -> None:
        if len(text) == 0 or text.isspace():
            raise ValueError(message)

    @staticmethod
    def alphanumeric_with_spaces(text: str, message: str) -> None:
        if not all(char.isalnum() or char.isspace() for char in text):
            raise ValueError(message)
        
    @staticmethod
    def duplicate_name(name: str, attribute: str, collection: list, message: str) -> None:
        if any(getattr(x, attribute) == name for x in collection):
            raise ValueError(message)
        