class Validation:

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

    @staticmethod
    def is_string_len_under(text: str, symbols_count: int, message: str) -> None:
        if len(text.strip()) < symbols_count:
            raise ValueError(message)

    @staticmethod
    def is_string_only_letters_and_numbers(text: str, message: str) -> None:
        if not text.isalnum():
            raise ValueError(message)
