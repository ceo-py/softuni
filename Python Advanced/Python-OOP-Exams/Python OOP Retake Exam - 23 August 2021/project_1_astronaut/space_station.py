from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.validation.validation import Validation


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.mission_report = {" successful missions!": 0, " missions were not completed!": 0}

    @property
    def astronaut_create(self):
        return {"Biologist": Biologist,
                "Geodesist": Geodesist,
                "Meteorologist": Meteorologist}

    def add_astronaut(self, astronaut_type: str, name: str):
        Validation.space_station_astronaut_types(astronaut_type)

        if any(name == a.name for a in self.astronaut_repository.astronauts):
            return f"{name} is already added."

        new_astronaut = self.astronaut_create[astronaut_type](name)
        self.astronaut_repository.add(new_astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if any(name == p.name for p in self.planet_repository.planets):
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items += items.split(", ")
        self.planet_repository.add(new_planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        Validation.space_station_astronaut_exists(name, self.astronaut_repository.astronauts)
        for pos, a in enumerate(self.astronaut_repository.astronauts):
            if name == a.name:
                del self.astronaut_repository.astronauts[pos]
                return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        Validation.space_station_planer_name(planet_name, self.planet_repository.planets)

        astronauts = [a for a in sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)]
        Validation.space_station_suitable_astronauts(self.astronaut_repository.astronauts)
        astronauts_top5 = [a for a in astronauts if a.oxygen > 30][:5]
        current_planet = [p for p in self.planet_repository.planets if p.name == planet_name][0]

        for a in astronauts_top5:
            while current_planet.items and a.oxygen > 0:
                a.backpack.append(current_planet.items.pop())
                a.breathe()

        if current_planet.items:
            self.mission_report[" missions were not completed!"] += 1
            return "Mission is not completed."

        self.mission_report[" successful missions!"] += 1
        return f"Planet: {planet_name} was explored. {len([a for a in astronauts_top5 if a.backpack])} astronauts participated in collecting items."

    def report(self):
        output = []
        for k, v in self.mission_report.items():
            output.append(f"{v}{k}")

        output.append("Astronauts' info:")
        for a in self.astronaut_repository.astronauts:
            output.append(f"Name: {a.name}")
            output.append(f"Oxygen: {a.oxygen}")
            if a.backpack:
                output.append(f"Backpack items: {', '.join(a.backpack)}")
            else:
                output.append(f"Backpack items: none")
        return "\n".join(output)

