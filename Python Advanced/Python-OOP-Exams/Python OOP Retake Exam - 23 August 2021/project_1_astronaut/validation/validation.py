class Validation:

    @staticmethod
    def astronaut_name(name: str):
        if len(name) == 0 or name.isspace():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

    @staticmethod
    def planet_name(name: str):
        if len(name) == 0 or name.isspace():
            raise ValueError("Planet name cannot be empty string or whitespace!")

    @staticmethod
    def space_station_astronaut_types(type_astronaut: str):
        if type_astronaut not in ("Biologist", "Geodesist", "Meteorologist"):
            raise Exception("Astronaut type is not valid!")

    @staticmethod
    def space_station_astronaut_exists(astronaut_name: str, astronauts: list):
        if all(astronaut_name != a.name for a in astronauts):
            raise Exception(f"Astronaut {astronaut_name} doesn't exist!")

    @staticmethod
    def space_station_planer_name(planet_name: str, planets: list):
        if all(planet_name != p.name for p in planets):
            raise Exception("Invalid planet name!")

    @staticmethod
    def space_station_suitable_astronauts(astronauts: list):
        if all(a.oxygen <= 30 for a in astronauts):
            raise Exception("You need at least one astronaut to explore the planet!")



