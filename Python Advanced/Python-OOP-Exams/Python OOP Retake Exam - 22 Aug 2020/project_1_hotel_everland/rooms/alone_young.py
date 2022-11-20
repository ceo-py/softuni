from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    default_room_members = 1
    room_cost = 10
    appliances = [TV()] * default_room_members

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self.default_room_members)
        self.calculate_expenses(self.appliances)

