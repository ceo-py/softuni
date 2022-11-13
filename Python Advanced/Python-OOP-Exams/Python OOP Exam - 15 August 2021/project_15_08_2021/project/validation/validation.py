class Validation:

    @staticmethod
    def name(name: str, type_text: str):
        if len(name) == 0 or name.isspace():
            raise ValueError(f"{type_text} cannot be empty string or white space!")

    @staticmethod
    def positive_number(price: float, type_text: str):
        if price <= 0:
            raise ValueError(f"{type_text} cannot be less than or equal to zero!")

    @staticmethod
    def table_capacity(capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity has to be greater than 0!")

    @staticmethod
    def table_number(number: int, min_people: int, max_people: int, table_side: str):
        if not min_people <= number <= max_people:
            raise ValueError(f"{table_side} table's number must be between {min_people} and {max_people} inclusive!")

    @staticmethod
    def bakery_food_or_drink_duplicate(food_or_drink_type: str, name: str, food_or_drink_list: list):
        if any(name == f.name for f in food_or_drink_list):
            raise Exception(f"{food_or_drink_type} {name} is already in the menu!")

    @staticmethod
    def bakery_table_duplicate(number: int, all_tables: list):
        if any(number == t.table_number for t in all_tables):
            raise Exception(f"Table {number} is already in the bakery!")

