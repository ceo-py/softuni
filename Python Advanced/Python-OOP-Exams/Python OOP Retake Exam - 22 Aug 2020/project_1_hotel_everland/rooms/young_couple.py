from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    default_room_members = 2
    room_cost = 20
    appliances = [TV(), Fridge(), Laptop()] * default_room_members

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, self.default_room_members)
        self.calculate_expenses(self.appliances)
