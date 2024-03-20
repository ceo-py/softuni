from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, ScubaDiver.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        if self.is_oxygen_level_enough(time_to_catch):
            self.oxygen_level -= int(time_to_catch * 0.30)

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.OXYGEN_LEVEL
