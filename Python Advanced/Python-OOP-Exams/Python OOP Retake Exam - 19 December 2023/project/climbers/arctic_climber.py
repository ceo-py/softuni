from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200

    def __init__(self, name: str):
        super().__init__(name, strength=ArcticClimber.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= 100
    
    def climb(self, peak: BasePeak):
        base_reduced_strength = 20
        base_multiplied_strength = 1.5
        
        if peak.difficulty_level == 'Extreme':
            base_multiplied_strength = 2

        self.strength -= base_reduced_strength * base_multiplied_strength
        self.conquered_peaks.append(peak.name)