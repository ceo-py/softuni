from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver

from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


class NauticalCatchChallengeApp:

    def __init__(self):
        self.divers: list = []
        self.fish_list: list = []

    def __find_object(self, item: str, attribute: str, type_object: str):
        if type_object == "fish":
            collection = self.fish_list
        elif type_object == "diver":
            collection = self.divers

        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    @property
    def divers_type(self):
        return {
            "ScubaDiver": ScubaDiver,
            "FreeDiver": FreeDiver
        }

    @property
    def fish_type(self):
        return {
            "PredatoryFish": PredatoryFish,
            "DeepSeaFish": DeepSeaFish
        }

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.divers_type:
            return f'{diver_type} is not allowed in our competition.'

        diver = self.__find_object(diver_name, "name", "diver")
        if diver:
            return f'{diver_name} is already a participant.'

        self.divers.append(self.divers_type[diver_type](diver_name))
        return f'{diver_name} is successfully registered for the competition as a {diver_type}.'

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.fish_type:
            return f'{fish_type} is forbidden for chasing in our competition.'

        fish = self.__find_object(fish_name, "name", "fish")
        if fish:
            return f'{fish_name} is already permitted.'

        self.fish_list.append(self.fish_type[fish_type](fish_name, points))
        return f'{fish_name} is allowed for chasing as a {fish_type}.'

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.__find_object(diver_name, "name", "diver")
        if not diver:
            return f'{diver_name} is not registered for the competition.'

        fish = self.__find_object(fish_name, "name", "fish")
        if not fish:
            return f'The {fish_name} is not allowed to be caught in this competition.'

        if diver.has_health_issue:
            return f'{diver_name} will not be allowed to dive, due to health issues.'

        if not diver.is_oxygen_level_enough(fish.time_to_catch):
            diver.update_health_status()
            diver.miss(fish.time_to_catch)
            return f'{diver.name} missed a good {fish.name}.'

        if diver.oxygen_level == fish.time_to_catch:
            diver.update_health_status()
            if is_lucky:
                diver.hit(fish)
                return f'{diver_name} hits a {fish.points}pt. {fish_name}.'

            diver.miss(fish.time_to_catch)
            return f'{diver_name} missed a good {fish_name}.'

        diver.hit(fish)
        return f'{diver_name} hits a {fish.points}pt. {fish_name}.'

    def health_recovery(self):
        count_health_issue = 0

        for diver in self.divers:
            if diver.has_health_issue:
                count_health_issue += 1
                diver.update_health_status()
                diver.renew_oxy()

        return f'Divers recovered: {count_health_issue}'

    def diver_catch_report(self, diver_name: str):
        diver = self.__find_object(diver_name, "name", "diver")
        return '\n'.join([f'**{diver_name} Catch Report**',
                          *[str(f.fish_details()) for f in diver.catch]])

    def competition_statistics(self):
        output = ['**Nautical Catch Challenge Statistics**']
        drivers_in_good_health = [
            d for d in self.divers if not d.has_health_issue]
        [output.append(str(d)) for d in sorted(drivers_in_good_health,
                                               key=lambda x: [-x.competition_points, -len(x.catch), x.name])]

        return '\n'.join(output)
