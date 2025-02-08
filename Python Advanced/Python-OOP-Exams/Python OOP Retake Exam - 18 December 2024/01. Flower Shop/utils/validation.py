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
    def is_name_two_char(name: str, limit: int, message: str) -> None:
        if len(name.strip()) < limit:
            raise ValueError(message)

    @staticmethod
    def is_only_digits(number: str, message: str) -> None:
        if not all(digit.isdigit() for digit in number):
            raise ValueError(message)
        
    @staticmethod
    def empty_string_or_empty_spaces(text: str, message: str) -> None:
        if len(text) == 0 or text.isspace():
            raise ValueError(message)
        
    @staticmethod
    def duplicate_attribute(attribute_content: str, attribute: str, collection: list, message: str) -> None:
        if any(getattr(x, attribute) == attribute_content for x in collection):
            raise ValueError(message)

    @staticmethod
    def valid_collection(name: str, collection: list, message: str) -> None:
        if name not in collection:
            raise ValueError(message)
        