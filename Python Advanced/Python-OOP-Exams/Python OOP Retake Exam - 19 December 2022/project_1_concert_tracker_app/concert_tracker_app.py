from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert
from project.validation.validation import Validation


class ConcertTrackerApp:

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    @property
    def correct_musicians(self):
        return {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    @staticmethod
    def __find_object(searching_for: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == searching_for:
                return obj

    def create_musician(self, musician_type: str, name: str, age: int):
        Validation.check_if_item_is_in_items(musician_type, self.correct_musicians, "Invalid musician type!")
        Validation.check_for_duplicity(name, self.musicians, "name", f"{name} is already a musician!")

        self.musicians.append(self.correct_musicians[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        Validation.check_for_duplicity(name, self.bands, "name", f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.__find_object(place, "place", self.concerts)
        if concert:
            genre = concert.genre
        Validation.check_for_duplicity(place, self.concerts, "place",
                                       f"{place} is already registered for {genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__find_object(musician_name, "name", self.musicians)
        Validation.check_if_object_with_given_name_exists(musician, f"{musician_name} isn't a musician!")

        band = self.__find_object(band_name, "name", self.bands)
        Validation.check_if_object_with_given_name_exists(band, f"{band_name} isn't a band!")

        return band.add_musician(musician)

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.__find_object(band_name, "name", self.bands)
        Validation.check_if_object_with_given_name_exists(band, f"{band_name} isn't a band!")

        musician = band.find_musician(musician_name)
        Validation.check_if_object_with_given_name_exists(musician, f"{musician_name} isn't a member of {band_name}!")

        return band.remove_musician(musician)

    def start_concert(self, concert_place: str, band_name: str):
        concert = self.__find_object(concert_place, "place", self.concerts)
        band = self.__find_object(band_name, "name", self.bands)

        band.have_enough_members_to_play_concert(self.correct_musicians)
        band.can_band_play_concert(concert.needed_musicians_and_skills[concert.genre])

        return f"{band_name} gained {concert.profit:.2f}$ from the {concert.genre} concert in {concert_place}."
