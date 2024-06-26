class Validation:

    @staticmethod
    def is_correct_type(type_: str, collection: list, message: str) -> None:
        if not any(x in type_ for x in collection):
            raise ValueError(message)

    @staticmethod
    def is_number_in_range(number: int, min_value: int, max_value: int, message: str) -> None:
        if not min_value <= number <= max_value:
            raise ValueError(message)

    @staticmethod
    def is_number_under(number: int, limit: int, message) -> None:
        if number < limit:
            raise ValueError(message)

    @staticmethod
    def is_empty_string(text: str, message: str) -> None:
        if len(text) == 0 or text.isspace():
            raise ValueError(message)
