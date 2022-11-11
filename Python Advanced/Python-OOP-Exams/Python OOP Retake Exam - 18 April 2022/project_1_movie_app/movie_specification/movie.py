from abc import ABC, abstractmethod
from project.validation.validation import Validation


class Movie(ABC):
    @abstractmethod
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        Validation.movie_title(value)
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        Validation.movie_year(value)
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        Validation.movie_owner(value)
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        Validation.age_restriction(value, self)
        self.__age_restriction = value

    def details(self):
        return f"{self.__class__.__name__} - Title:{self.title}, " \
               f"Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, " \
               f"Owned by:{self.owner.username}"
