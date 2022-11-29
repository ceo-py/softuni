class Validation:

    @staticmethod
    def name_empty_string_or_white_spaces(name: str, message: str):
        if name == "" or name.isspace():
            raise ValueError(message)

    @staticmethod
    def jokey_age_over_17(age: int, message: str):
        if age < 18:
            raise ValueError(message)

    @staticmethod
    def name_horse_less_than_4(name: str, message: str):
        if len(name) < 4:
            raise ValueError(message)

    @staticmethod
    def speed_limit(speed: int, limit_speed: int, message: str):
        if speed > limit_speed:
            raise ValueError(message)

    @staticmethod
    def four_season_race(race_type: str, message: str):
        if race_type not in ("Winter", "Spring", "Autumn", "Summer"):
            raise ValueError(message)

    @staticmethod
    def horse_name_duplicate(horse_name: str, horse_list: [], message: str):
        if any(h.name == horse_name for h in horse_list):
            raise Exception(message)

    @staticmethod
    def jockey_name_duplicate(jockey_name: str, jockey_list: [], message: str):
        if any(j.name == jockey_name for j in jockey_list):
            raise Exception(message)

    @staticmethod
    def horse_race_one_of_type_created(race_type: str, race_list: [], message: str):
        if any(r.race_type == race_type for r in race_list):
            raise Exception(message)

    @staticmethod
    def jockey_exist(jockey_name: str, jockey_list: [], message: str):
        if all(j.name != jockey_name for j in jockey_list):
            raise Exception(message)

    @staticmethod
    def horse_available(horse_type: str, horse_list: [], message: str):
        if all(h.is_taken for h in horse_list) or all(h.__class__.__name__ != horse_type for h in horse_list):
            raise Exception(message)

    @staticmethod
    def horse_race_exist(race_type: str, race_list: [], message: str):
        if all(r.race_type != race_type for r in race_list):
            raise Exception(message)

    @staticmethod
    def jockey_have_horse(jockey_object: object, message: str):
        if jockey_object.horse is None:
            raise Exception(message)

    @staticmethod
    def jockey_already_in_the_race(jockey_name: str, race_jockeys: list, message: str):
        if any(j.name == jockey_name for j in race_jockeys):
            raise Exception(message)

    @staticmethod
    def race_minimum_two_members(race_participants: list, message: str):
        if len(race_participants) < 2:
            raise Exception(message)




