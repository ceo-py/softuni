from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150

    def __init__(self, name: str):
        super().__init__(name, strength=SummitClimber.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        base_reduced_strength = 30
        base_multiplied_strength = 2.5

        if peak.difficulty_level == 'Advanced':
            base_multiplied_strength = 1.3

        self.strength -= base_reduced_strength * base_multiplied_strength
        self.conquered_peaks.append(peak.name)
