from project.validation.validation import Validation


class Concert:

    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    @property
    def profit(self):
        return (self.audience * self.ticket_price) - self.expenses

    @property
    def needed_musicians_and_skills(self):
        return \
            {"Metal": {
                "Drummer": ["play the drums with drumsticks"],
                "Singer": ["sing low pitch notes"],
                "Guitarist": ["play metal"],
            }, "Rock": {
                "Drummer": ["play the drums with drumsticks"],
                "Singer": ["sing high pitch notes"],
                "Guitarist": ["play rock"],
            }, "Jazz": {
                "Drummer": ["play the drums with drum brushes"],
                "Singer": ["sing high pitch notes", "sing low pitch notes"],
                "Guitarist": ["play jazz"],
            }
            }

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        Validation.check_if_item_is_in_items(value, self.needed_musicians_and_skills,
                                             f"Our group doesn't play {value}!")
        self.__genre = value

    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value):
        Validation.check_number_less_than(value, 1, "At least one person should attend the concert!")
        self.__audience = value

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        Validation.check_number_less_than(value, 1, "Ticket price must be at least 1.00$!")
        self.__ticket_price = value

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        Validation.check_number_less_than(value, 0,"Expenses cannot be a negative number!")
        self.__expenses = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        Validation.check_if_string_is_two_characters_long(value, "Place must contain at least 2 chars. It cannot be empty!")
        self.__place = value

    def __str__(self):
        return f"{self.genre} concert at {self.place}."
