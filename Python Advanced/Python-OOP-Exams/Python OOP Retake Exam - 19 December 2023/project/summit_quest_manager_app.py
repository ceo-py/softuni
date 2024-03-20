from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:

    def __init__(self):
        self.climbers: list = []
        self.peaks: list = []

    @staticmethod
    def __find_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    @property
    def __climbers(self):
        return {
            'ArcticClimber': ArcticClimber,
            'SummitClimber': SummitClimber,
        }

    @property
    def __peaks(self):
        return {
            'ArcticPeak': ArcticPeak,
            'SummitPeak': SummitPeak,
        }

    def register_climber(self, climber_type: str, climber_name: str) -> str:
        if climber_type not in self.__climbers:
            return f"{climber_type} doesn't exist in our register."

        found_climber = self.__find_object(climber_name, 'name', self.climbers)
        if found_climber:
            return f'{climber_name} has been already registered.'

        self.climbers.append(self.__climbers[climber_type](climber_name))
        return f'{climber_name} is successfully registered as a {climber_type}.'

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int) -> str:
        if peak_type not in self.__peaks:
            return f'{peak_type} is an unknown type of peak.'

        self.peaks.append(self.__peaks[peak_type](peak_name, peak_elevation))
        return f'{peak_name} is successfully added to the wish list as a {peak_type}.'

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):

        peak = self.__find_object(peak_name, 'name', self.peaks)
        climber = self.__find_object(climber_name, 'name', self.climbers)

        missing_gear = [
            gear_item for gear_item in peak.get_recommended_gear() if gear_item not in gear
        ]
        if missing_gear:
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

        return f'{climber_name} is prepared to climb {peak_name}.'

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self.__find_object(climber_name, 'name', self.climbers)
        if not climber:
            return f'Climber {climber_name} is not registered yet.'

        peak = self.__find_object(peak_name, 'name', self.peaks)
        if not peak:
            return f'Peak {peak_name} is not part of the wish list.'

        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f'{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}.'

        elif not climber.is_prepared:
            return f'{climber_name} will need to be better prepared next time.'

        else:
            climber.rest()
            return f'{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest.'

    def get_statistics(self):
        output = []
        climbers_conquer_peaks = []

        for c in self.climbers:
            if c.conquered_peaks:
                c.sort_conquered_peaks()
                climbers_conquer_peaks.append(c)

        output.append(
            f'Total climbed peaks: {len(set([peak for c in climbers_conquer_peaks for peak in c.conquered_peaks]))}')
        output.append("**Climber's statistics:**")
        output.extend(
            str(climber) for climber in sorted(climbers_conquer_peaks, key=lambda x: (-len(x.conquered_peaks), x.name)))

        return '\n'.join(output)
