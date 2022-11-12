from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.validation.validation import Validation
from project.driver import Driver
from project.race import Race


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    @property
    def __car_types(self):
        return {"MuscleCar": MuscleCar,
                "SportsCar": SportsCar}

    def __get_driver(self, driver_name):
        for d in self.drivers:
            if driver_name == d.name:
                return d

    def __get_race(self, race_name):
        for r in self.races:
            if race_name == r.name:
                return r

    def __get_car(self, car_type):
        return [c for c in self.cars if car_type == c.__class__.__name__ and not c.is_taken][-1]

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.__car_types:
            return

        Validation.controller_duplicate_car(model, self.cars)
        new_car = self.__car_types[car_type](model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        Validation.controller_duplicate_driver(driver_name, self.drivers)
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        Validation.controller_duplicate_race(race_name, self.races)

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        Validation.controller_driver_exists(driver_name, self.drivers)
        Validation.controller_car_available(car_type, self.cars)

        current_driver = self.__get_driver(driver_name)
        current_car = self.__get_car(car_type)
        current_car.is_taken = True

        if current_driver.car:
            old_model = current_driver.car
            old_model.is_taken = False
            current_driver.car = current_car
            return f"Driver {driver_name} changed his car from {old_model.model} to {current_car.model}."

        current_driver.car = current_car
        return f"Driver {driver_name} chose the car {current_driver.car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        Validation.controller_race_exists(race_name, self.races)
        Validation.controller_driver_exists(driver_name, self.drivers)

        current_driver = self.__get_driver(driver_name)
        Validation.controller_driver_own_car(current_driver)

        current_race = self.__get_race(race_name)
        if any(driver_name == d.name for d in current_race.drivers):
            return f"Driver {driver_name} is already added in {race_name} race."

        current_race.drivers.append(current_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        Validation.controller_race_exists(race_name, self.races)

        current_race = self.__get_race(race_name)
        Validation.controller_race_participants(current_race)

        winners = [d for d in sorted(current_race.drivers, key=lambda x: -x.car.speed_limit)][:3]

        output = []
        for d in winners:
            d.number_of_wins += 1
            output.append(f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}.")

        return "\n".join(output)
