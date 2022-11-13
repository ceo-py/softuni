from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.validation.validation import Validation


class Bakery:

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0
        self.__total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.name(value, "Name")
        self.__name = value

    @property
    def __food_types(self):
        return {"Bread": Bread,
                "Cake": Cake}

    @property
    def __drink_types(self):
        return {"Tea": Tea,
                "Water": Water}

    @property
    def __table_types(self):
        return {"InsideTable": InsideTable,
                "OutsideTable": OutsideTable}

    def __find_table(self, number: int):
        for t in self.tables_repository:
            if t.table_number == number:
                return t

    def __get_menu(self):
        menu = {f.name: f for f in self.food_menu}
        menu.update({d.name: d for d in self.drinks_menu})
        return menu

    def __order_items(self, table: object, items_name: list, type_items: str):
        menu = self.__get_menu()
        items_can_be_order, items_not_in_menu = [], []

        for items in items_name:
            if items in menu and type_items == "Food":
                table.order_food(menu[items])
                items_can_be_order.append(str(menu[items]))
            elif items in menu and type_items == "Drink":
                table.order_drink(menu[items])
                items_can_be_order.append(str(menu[items]))
            else:
                items_not_in_menu.append(items)

        output = [f"Table {table.table_number} ordered:"]
        for items in items_can_be_order:
            output.append(items)

        output.append(f"{self.name} does not have in the menu:")
        for items in items_not_in_menu:
            output.append(items)

        return "\n".join(output)

    def add_food(self, food_type: str, name: str, price: float):
        Validation.bakery_food_or_drink_duplicate(food_type, name, self.food_menu)

        if food_type in self.__food_types:
            new_food = self.__food_types[food_type](name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        Validation.bakery_food_or_drink_duplicate(drink_type, name, self.drinks_menu)

        if drink_type in self.__drink_types:
            new_drink = self.__drink_types[drink_type](name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        Validation.bakery_table_duplicate(table_number, self.tables_repository)

        if table_type in self.__table_types:
            new_table = self.__table_types[table_type](table_number, capacity)
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        find_table = [t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people]
        if find_table:
            find_table = find_table[0]
            find_table.reserve(number_of_people)
            return f"Table {find_table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: tuple):
        table = self.__find_table(table_number)

        if not table:
            return f"Could not find table {table_number}"

        return self.__order_items(table, food_names, "Food")

    def order_drink(self, table_number: int, *drink_names: tuple):
        table = self.__find_table(table_number)

        if not table:
            return f"Could not find table {table_number}"

        return self.__order_items(table, drink_names, "Drink")

    def leave_table(self, table_number: int):
        table = self.__find_table(table_number)
        if table:
            table_bill, table_number = table.get_bill(), table.table_number
            self.__total_income += table_bill
            table.clear()
            return f"Table: {table_number}\n" \
                   f"Bill: {table_bill:.2f}"

    def get_free_tables_info(self):
        return "\n".join(t.free_table_info() for t in self.tables_repository)

    def get_total_income(self):
        return f"Total income: {self.__total_income:.2f}lv"
