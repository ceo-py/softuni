from project.teams.base_team import BaseTeam
class IndoorTeam(BaseTeam):
    BUDGET = 500

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=IndoorTeam.BUDGET)
        self.team_type = 'IndoorTeam'

    
    def win(self):
        self.wins += 1
        self.advantage += 145