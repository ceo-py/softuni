from project.util.vd import Validation

from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad

from project.teams.outdoor_team import OutdoorTeam
from project.teams.indoor_team import IndoorTeam

from typing import List, Union


class Tournament:

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[Union[KneePad, ElbowPad]] = []
        self.teams: List[Union[OutdoorTeam, IndoorTeam]] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        Validation.is_string_only_letters_and_numbers(
            value, 'Tournament name should contain letters and digits only!')
        self.__name = value

    @property
    def equipment_type(self):
        return {
            'KneePad': KneePad,
            'ElbowPad': ElbowPad,
        }

    @property
    def team_type(self):
        return {
            'OutdoorTeam': OutdoorTeam,
            'IndoorTeam': IndoorTeam,
        }

    @staticmethod
    def __find_object(item: str, attribute: str, collection: list) -> Union[KneePad, ElbowPad, IndoorTeam, OutdoorTeam]:
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    @staticmethod
    def get_last_found_item_in_collection(item: str, attribute: str, collection: list) -> Union[KneePad, ElbowPad]:
        for i in range(len(collection) - 1, -1, -1):
            obj = collection[i]
            if getattr(obj, attribute) == item:
                return obj

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.equipment_type:
            raise Exception('Invalid equipment type!')

        self.equipment.append(self.equipment_type[equipment_type]())
        return f'{equipment_type} was successfully added.'

    def remove_equipment_from_collection(self, equipment: Union[ElbowPad, KneePad]) -> None:
        self.equipment.remove(equipment)

    def remove_team_from_collection(self, team: Union[IndoorTeam, OutdoorTeam]) -> None:
        self.teams.remove(team)

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.team_type:
            raise Exception('Invalid team type!')

        if self.capacity == 0:
            return 'Not enough tournament capacity.'

        self.capacity -= 1
        self.teams.append(self.team_type[team_type](
            team_name, country, advantage))
        return f'{team_type} was successfully added.'

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = self.__find_object(team_name, 'name', self.teams)
        equipment = self.get_last_found_item_in_collection(
            equipment_type, 'type_equipment', self.equipment)

        if equipment.price > team.budget:
            raise Exception('Budget is not enough!')

        self.remove_equipment_from_collection(equipment)
        team.budget -= equipment.price
        team.equipment.append(equipment)
        return f'Successfully sold {equipment_type} to {team_name}.'

    def remove_team(self, team_name: str):
        team = self.__find_object(team_name, 'name', self.teams)

        if not team:
            raise Exception('No such team!')

        if team.wins > 0:
            raise Exception(
                f'The team has {team.wins} wins! Removal is impossible!')

        self.capacity += 1
        self.remove_team_from_collection(team)
        return f'Successfully removed {team_name}.'

    def increase_equipment_price(self, equipment_type: str):
        count_increase_price = 0
        for equipment in self.equipment:
            if equipment.type_equipment != equipment_type:
                continue
            equipment.increase_price()
            count_increase_price += 1

        return f'Successfully changed {count_increase_price}pcs of equipment.'

    def play(self, team_name1: str, team_name2: str):
        team1 = self.__find_object(team_name1, 'name', self.teams)
        team2 = self.__find_object(team_name2, 'name', self.teams)

        if team1.team_type != team2.team_type:
            raise Exception('Game cannot start! Team types mismatch!')

        teams_compete = {
            'team1': {
                'team': team1,
                'score': team1.team_score()
            },
            'team2': {
                'team': team2,
                'score': team2.team_score()
            },
        }
        team_with_max_score = max(
            teams_compete, key=lambda x: teams_compete[x]['score'])

        if teams_compete['team1']['score'] == teams_compete['team2']['score']:
            return 'No winner in this game.'

        winner = teams_compete[team_with_max_score]['team']
        winner.win()
        return f'The winner is {winner.name}.'

    def get_statistics(self):
        output = [
            f'Tournament: {self.name}',
            f'Number of Teams: {len(self.teams)}',
            f'Teams:',
            *[t.get_statistics()
              for t in sorted(self.teams, key=lambda x: -x.wins)],
        ]

        return '\n'.join(output)
