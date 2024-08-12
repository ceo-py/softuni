class Validation:


    @staticmethod
    def white_space_or_less_than_three_characters(text: str, message: str) -> None:
        if len(text) < 3 or text.isspace():
            raise ValueError(message)

    @staticmethod
    def is_number_under(number: float, limit: float, message: str) -> None:
        if number < limit:
            raise ValueError(message)
        
    @staticmethod
    def empty_string_or_empty_spaces(text: str, message: str) -> None:
        if len(text) == 0 or text.isspace():
            raise ValueError(message)
        
    @staticmethod
    def exact_three_characters(text: str, message: str) -> None:
        if len(text) != 3 or " " in text:
            raise ValueError(message)
        
    @staticmethod
    def valid_types(type_: str, types: dict, message: str) -> None:
        if not types.get(type_):
            raise Exception(message)
        
    @staticmethod
    def store_with_name_exists(store_name: str, stores:list, message: str) -> None:
        if all(s.name != store_name for s in stores):
            raise Exception(message)
