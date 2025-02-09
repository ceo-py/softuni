class Validation:


    @staticmethod
    def is_all_letters(text: str, message: str) -> None:
        if not text.isalpha():
            raise ValueError(message)
    @staticmethod
    def is_all_digits(text: str, message: str) -> None:
        if not text.isdigit():
            raise ValueError(message)

    @staticmethod
    def is_duplicate_by_attribute(attribute_content: str, attribute: str, collection: list, message: str) -> None:
        if any(getattr(x, attribute) == attribute_content for x in collection):
            raise Exception(message)

        