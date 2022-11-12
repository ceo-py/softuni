class Validation:

    @staticmethod
    def car_model(model: str):
        if len(model) < 4:
            raise ValueError(f"Model {model} is less than 4 symbols!")

    @staticmethod
    def car_speed_limit(speed: int, speed_limit_min: int, speed_limit_max: int):
        if speed_limit_min > speed or speed > speed_limit_max:
            raise ValueError(f"Invalid speed limit! Must be between {speed_limit_min} and {speed_limit_max}!")

    @staticmethod
    def driver_name(name: str):
        if len(name) == 0 or name.isspace():
            raise ValueError("Name should contain at least one character!")

    @staticmethod
    def race_name(name: str):
        if len(name) == 0:
            raise ValueError("Name cannot be an empty string!")

    @staticmethod
    def controller_duplicate_car(model: str, cars_list: list):
        if any(model == c.model for c in cars_list):
            raise Exception(f"Car {model} is already created!")

    @staticmethod
    def controller_duplicate_driver(driver_name: str, driver_list: list):
        if any(driver_name == d.name for d in driver_list):
            raise Exception(f"Driver {driver_name} is already created!")

    @staticmethod
    def controller_duplicate_race(race_name: str, race_list: list):
        if any(race_name == r.name for r in race_list):
            raise Exception(f"Race {race_name} is already created!")

    @staticmethod
    def controller_driver_exists(driver_name: str, driver_list: list):
        if all(driver_name != d.name for d in driver_list):
            raise Exception(f"Driver {driver_name} could not be found!")

    @staticmethod
    def controller_car_available(type_car: str, cars_list: list):
        if all(type_car == d.__class__.__name__ and d.is_taken for d in cars_list) or \
                all(type_car != d.__class__.__name__ for d in cars_list):
            raise Exception(f"Car {type_car} could not be found!")

    @staticmethod
    def controller_race_exists(race_name: str, race_list: list):
        if all(race_name != r.name for r in race_list):
            raise Exception(f"Race {race_name} could not be found!")

    @staticmethod
    def controller_driver_own_car(driver: object):
        if driver.car is None:
            raise Exception(f"Driver {driver.name} could not participate in the race!")

    @staticmethod
    def controller_race_participants(race: object):
        if len(race.drivers) < 3:
            raise Exception(f"Race {race.name} cannot start with less than 3 participants!")
