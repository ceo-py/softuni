from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.validation.validation import Validation


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    @property
    def __type_of_delicacy(self):
        return {"Gingerbread": Gingerbread,
                "Stolen": Stolen}

    @property
    def __type_of_booth(self):
        return {"Open Booth": OpenBooth,
                "Private Booth": PrivateBooth}

    def __find_booth_to_reserve(self, number_of_people: int):
        for b in self.booths:
            if not b.is_reserved and b.capacity >= number_of_people:
                return b

    def __find_booth_by_number(self, booth_number: int):
        for b in self.booths:
            if b.booth_number == booth_number:
                return b

    def __find_delicacy_by_name(self, delicacy_name):
        for d in self.delicacies:
            if d.name == delicacy_name:
                return d

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        Validation.item_duplicity(name, self.delicacies, f"{name} already exists!")
        Validation.correct_type(type_delicacy, self.__type_of_delicacy, f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.__type_of_delicacy[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        Validation.number_duplicity(booth_number, self.booths, f"Booth number {booth_number} already exists!")
        Validation.correct_type(type_booth, self.__type_of_booth, f"{type_booth} is not a valid booth!")

        new_booth = self.__type_of_booth[type_booth](booth_number, capacity)
        self.booths.append(new_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = self.__find_booth_to_reserve(number_of_people)

        Validation.item_not_found(booth, f"No available booth for {number_of_people} people!")
        booth.reserve(number_of_people)

        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth_by_number(booth_number)

        Validation.item_not_found(booth, f"Could not find booth {booth_number}!")

        delicacy = self.__find_delicacy_by_name(delicacy_name)
        Validation.item_not_found(delicacy, f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth_by_number(booth_number)
        bill = booth.calculate_bill()
        self.income += bill
        booth.leave_booth()

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."


