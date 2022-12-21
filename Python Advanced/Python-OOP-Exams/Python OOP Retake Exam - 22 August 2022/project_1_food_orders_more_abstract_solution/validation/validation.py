class Validation:
    type_errors = {
        "value error": ValueError,
        "exception": Exception
    }

    @staticmethod
    def phone_number(phone_number: str, type_error: str, message: str):
        if not phone_number.startswith("0") or len(phone_number) != 10 or not phone_number.isdigit():
            raise Validation.type_errors[type_error](message)

    @staticmethod
    def len_of_item_less(item: object, length: int, type_error: str, message: str):
        if len(item) < length:
            raise Validation.type_errors[type_error](message)

    @staticmethod
    def number_less_then_or_equal(number: float, compere_to: float, type_error: str, message: str):
        if number <= compere_to:
            raise Validation.type_errors[type_error](message)

    @staticmethod
    def duplicity_by_attribute(item: str, attribute: str, collection: list, type_error: str, message: str):
        if any(getattr(obj, attribute) == item for obj in collection):
            raise Validation.type_errors[type_error](message)

    @staticmethod
    def item_in_collection(item: str, collection: list, type_error: str, message: str):
        if item not in collection:
            raise Validation.type_errors[type_error](message)

    @staticmethod
    def quantity_enough(item: str, quantity: int, collection: list, type_error: str, message: str):
        if collection[item].quantity < quantity:
            raise Validation.type_errors[type_error](message)




