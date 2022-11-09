from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.validation.validation import Validation


class HorseRaceApp:
    horse_types = {"Appaloosa": Appaloosa,
                   "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        Validation.name_horse_duplicate(horse_name, self.horses)
        if horse_type in self.horse_types:
            self.horses.append(self.horse_types[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        Validation.name_jockey_duplicate(jockey_name, self.jockeys)

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def __get_horse(self, horse_type: str):
        return [h for h in self.horses if h.__class__.__name__ == horse_type][-1]

    def __get_jockey(self, name: str):
        for j in self.jockeys:
            if j.name == name:
                return j

    def __get_race(self, name: str):
        for r in self.horse_races:
            if r.race_type == name:
                return r

    def create_horse_race(self, race_type: str):
        Validation.race_type_duplicate(race_type, self.horse_races)

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        Validation.jockey_exist(jockey_name, self.jockeys)
        Validation.horse_available(horse_type, self.horses)

        horse = self.__get_horse(horse_type)
        jockey = self.__get_jockey(jockey_name)

        if not horse.is_taken and jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        Validation.horse_race_exist(race_type, self.horse_races)
        Validation.jockey_exist(jockey_name, self.jockeys)

        jockey = self.__get_jockey(jockey_name)

        Validation.jockey_have_horse(jockey)
        race = self.__get_race(race_type)
        if jockey_name in [j.name for j in race.jockeys]:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        Validation.horse_race_exist(race_type, self.horse_races)

        race = self.__get_race(race_type)
        Validation.min_race_participants(race)

        winner = None
        speed = 0
        for j in race.jockeys:
            if j.horse.speed > speed:
                speed = j.horse.speed
                winner = j

        return f"The winner of the {race_type} race, with a speed of {speed}km/h " \
               f"is {winner.name}! Winner's horse: {winner.horse.name}."







