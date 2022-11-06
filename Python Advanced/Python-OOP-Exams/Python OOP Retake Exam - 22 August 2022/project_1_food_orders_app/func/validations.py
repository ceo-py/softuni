class Validation:

    @staticmethod
    def phone_number(phone_number: str):
        if phone_number.startswith("0") and len(phone_number) == 10 and phone_number.isdigit():
            return True

        raise ValueError("Invalid phone number!")

    @staticmethod
    def empty_string(value):
        if value.strip() != "":
            return True

        raise ValueError("Name cannot be an empty string!")

    @staticmethod
    def check_positive_number(num):
        if num > 0:
            return True

        raise ValueError("Invalid price!")

    @staticmethod
    def check_menu(items):
        if len(items) < 5:
            raise Exception("The menu is not ready!")

    @staticmethod
    def empty_shopping_cart(data):
        if not data:
            raise Exception("There are no ordered meals!")


