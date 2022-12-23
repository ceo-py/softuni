from project.validation.validation import Validation


class Band:

    def __init__(self, name: str):
        self.name = name
        self.members = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.check_for_empty_string(value, "Band name should contain at least one character!")
        self.__name = value

    def add_musician(self, musician: object):
        self.members.append(musician)
        return f"{musician.name} was added to {self.name}."

    def find_musician(self, name: str):
        for m in self.members:
            if m.name == name:
                return m

    def remove_musician(self, musician: object):
        self.members.remove(musician)
        return f"{musician.name} was removed from {self.name}."

    def have_enough_members_to_play_concert(self, correct_musicians):
        all_types_musician_in_band = {type(m).__name__ for m in self.members}
        for type_musician in correct_musicians:
            if type_musician not in all_types_musician_in_band:
                Validation.check_band_one_of_each_type_musician(f"{self.name} can't start the concert because "
                                                                f"it doesn't have enough members!")

    def can_band_play_concert(self, musician_skills_needed: dict):
        all_musicians = []
        for musician, skills in musician_skills_needed.items():
            for band_musician in self.members:
                if type(band_musician).__name__ == musician and \
                        all(skill in band_musician.skills for skill in skills):
                    all_musicians.append(band_musician)

        Validation.check_band_members_have_the_skills(all_musicians, self.members,
                                                      f"The {self.name} band is not ready to play at the concert!")

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
