from project.booths.booth import Booth


class OpenBooth(Booth):
    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * 2.50
        self.is_reserved = True
