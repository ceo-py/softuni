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

    @staticmethod
    def existing_client(data_clients, client_phone_number):
        if any(x.phone_number == client_phone_number for x in data_clients):
            raise Exception("The client has already been registered!")

    @staticmethod
    def meal_in_menu(meal_names_and_quantities, menu_info):
        for meal in meal_names_and_quantities:
            if meal not in menu_info:
                raise Exception(f"{meal} is not on the menu!")

    @staticmethod
    def enough_quantity(meal_names_and_quantities, menu_info):
        for meal, quantity in meal_names_and_quantities.items():
            if menu_info[meal].quantity < quantity:
                raise Exception(f"Not enough quantity of {menu_info[meal].__class__.__name__}: {meal}!")


