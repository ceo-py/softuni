class Validation:

    @staticmethod
    def empty_string(name: str, sting_text: str):
        if len(name) == 0:
            raise ValueError(f"{sting_text} cannot be an empty string.")

    @staticmethod
    def number_below_zero(number: int):
        if number <= 0:
            raise ValueError("Price cannot be equal to or below zero.")

