from project.validation.validation import Validation


class User:
    INCREASE_RATING_BY = 0.5
    DECREASE_RATING_BY = 2.0
    UPPER_LIMIT_RATING = 10
    BOTTOM_LIMIT_RATING = 0

    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = 0
        self.is_blocked = False

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        Validation.empty_or_white_space(value, 'First name cannot be empty!')
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        Validation.empty_or_white_space(value, 'Last name cannot be empty!')
        self.__last_name = value

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        Validation.empty_or_white_space(value, 'Driving license number is required!')
        self.__driving_license_number = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        Validation.number_is_less_than(value, User.BOTTOM_LIMIT_RATING, 'Users rating cannot be negative!')
        self.__rating = value

    def increase_rating(self):
        self.rating += User.INCREASE_RATING_BY
        if self.rating > User.UPPER_LIMIT_RATING:
            self.rating = User.UPPER_LIMIT_RATING

    def decrease_rating(self):
        if self.rating - User.DECREASE_RATING_BY < User.BOTTOM_LIMIT_RATING:
            self.rating = User.BOTTOM_LIMIT_RATING
            self.is_blocked = True
            return

        self.rating -= User.DECREASE_RATING_BY

    def __str__(self):
        return f'{self.first_name} {self.last_name} Driving license: {self.driving_license_number} Rating: {self.rating}'
