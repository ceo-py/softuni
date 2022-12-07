from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, 1)
        self.room_cost = 10
