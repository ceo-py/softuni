class Validation:

    @staticmethod
    def string_less_than_symbols(name: str, max_symbols: int) -> None:
        if len(name) < max_symbols:
            raise ValueError(f"Peak name cannot be less than {max_symbols} symbols!")

    @staticmethod
    def is_number_under(number: int, limit: int, message) -> None:
        if number < limit:
            raise ValueError(message)

    @staticmethod
    def is_empty_string(text: str, message: str) -> None:
        if len(text) == 0 or text.isspace():
            raise ValueError(message)
