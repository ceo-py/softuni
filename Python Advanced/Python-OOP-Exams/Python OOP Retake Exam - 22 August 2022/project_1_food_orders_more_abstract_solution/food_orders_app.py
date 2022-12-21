from project.client import Client
from project.meals.meal import Meal
from project.validation.validation import Validation


class FoodOrdersApp:

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    @staticmethod
    def __find_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def __create_menu(self):
        return {m.name: m for m in self.menu}

    @staticmethod
    def __all_meals_on_menu(menu: dict, order: dict):
        for meal_name in order:
            Validation.item_in_collection(meal_name, menu, "exception", f"{meal_name} is not on the menu!")

    @staticmethod
    def __enough_quantity(menu: dict, order: dict):
        for meal_name, quantity in order.items():
            Validation.quantity_enough(meal_name, quantity, menu, "exception",
                                       f"Not enough quantity of {type(menu[meal_name]).__name__}: {meal_name}!")

    def register_client(self, client_phone_number: str):
        Validation.duplicity_by_attribute(client_phone_number, "phone_number", self.clients_list, "exception",
                                          "The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for m in meals:
            if type(m).__name__ in Meal.correct_meals:
                self.menu.append(m)

    def show_menu(self):
        Validation.len_of_item_less(self.menu, 5, "exception", "The menu is not ready!")

        return "\n".join(m.details() for m in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        Validation.len_of_item_less(self.menu, 5, "exception", "The menu is not ready!")

        client = self.__find_object(client_phone_number, "phone_number", self.clients_list)
        if client is None:
            self.register_client(client_phone_number)
            client = self.__find_object(client_phone_number, "phone_number", self.clients_list)

        menu = self.__create_menu()
        self.__all_meals_on_menu(menu, meal_names_and_quantities)
        self.__enough_quantity(menu, meal_names_and_quantities)

        client.add_meals_to_shopping_card(meal_names_and_quantities, menu)

        return f"Client {client_phone_number} successfully ordered {client.show_ordered_meals} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_object(client_phone_number, "phone_number", self.clients_list)
        Validation.len_of_item_less(client.shopping_cart, 1, "exception", "There are no ordered meals!")

        client.cancel_order_meals(self.__create_menu())
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_object(client_phone_number, "phone_number", self.clients_list)
        Validation.len_of_item_less(client.shopping_cart, 1, "exception", "There are no ordered meals!")
        bill = client.bill
        client.clear_order()
        self.receipt_id += 1

        return f"Receipt #{self.receipt_id} with total amount of {bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
