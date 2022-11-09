class Validation:

    @staticmethod
    def name_jockey(name: str):
        if name == "" or name.isspace():
            raise ValueError("Name should contain at least one character!")

    @staticmethod
    def age_jockey(age: int):
        if age < 18:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")

    @staticmethod
    def name_horse(name: str):
        if len(name) < 4:
            raise ValueError(f"Horse name {name} is less than 4 symbols!")

    @staticmethod
    def speed_horse(speed: int, maximum_speed: int):
        if speed > maximum_speed:
            raise ValueError("Horse speed is too high!")

    @staticmethod
    def race_type(season: str):
        if season not in ("Winter", "Spring", "Autumn", "Summer"):
            raise ValueError("Race type does not exist!")

    @staticmethod
    def name_horse_duplicate(name: str, names: list):
        if any(h.name == name for h in names):
            raise Exception(f"Horse {name} has been already added!")

    @staticmethod
    def name_jockey_duplicate(name: str, names: list):
        if any(j.name == name for j in names):
            raise Exception(f"Jockey {name} has been already added!")

    @staticmethod
    def race_type_duplicate(name: str, names: list):
        if any(r.race_type == name for r in names):
            raise Exception(f"Race {name} has been already created!")

    @staticmethod
    def jockey_exist(name: str, names: list):
        if name not in [n.name for n in names]:
            raise Exception(f"Jockey {name} could not be found!")

    @staticmethod
    def horse_available(horse: str, horse_type: list):
        if all(h.__class__.__name__ != horse for h in horse_type) or all(
                h.__class__.__name__ == horse and h.is_taken for h in horse_type):
            raise Exception(f"Horse breed {horse} could not be found!")

    @staticmethod
    def horse_race_exist(race_type: str, horse_races: list):
        if all(r.race_type != race_type for r in horse_races):
            raise Exception(f"Race {race_type} could not be found!")

    @staticmethod
    def jockey_have_horse(jockey):
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey.name} cannot race without a horse!")

    @staticmethod
    def min_race_participants(race):
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race.race_type} needs at least two participants!")




