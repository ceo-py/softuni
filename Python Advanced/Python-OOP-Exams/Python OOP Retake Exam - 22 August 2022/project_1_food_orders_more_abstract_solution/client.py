from project.validation.validation import Validation


class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.ordered_meals = {}
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        Validation.phone_number(value, "value error", "Invalid phone number!")
        self.__phone_number = value

    def add_meals_to_shopping_card(self, meals: dict, menu: dict):
        for meal, quantity in meals.items():
            self.bill += menu[meal].price * quantity
            menu[meal].reduce_quantity(quantity)
            self.ordered_meals[meal] = self.ordered_meals.get(meal, 0) + quantity
            self.shopping_cart.append(menu[meal])

    def cancel_order_meals(self, menu: dict):
        for meal, quantity in self.ordered_meals.items():
            menu[meal].add_quantity(quantity)
        self.clear_order()

    def clear_order(self):
        self.shopping_cart = []
        self.ordered_meals = {}
        self.bill = 0

    @property
    def show_ordered_meals(self):
        return ", ".join(m.name for m in self.shopping_cart)
