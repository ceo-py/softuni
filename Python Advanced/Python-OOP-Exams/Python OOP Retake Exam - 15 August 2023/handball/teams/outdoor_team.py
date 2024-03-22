from project.teams.base_team import BaseTeam
class OutdoorTeam(BaseTeam):
    BUDGET = 1000

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=OutdoorTeam.BUDGET)
        self.team_type = 'OutdoorTeam'


    def win(self):
        self.wins += 1
        self.advantage += 115