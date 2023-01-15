from project.formula_teams.formula_team import FormulaTeam
from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam
from project.validation.validation import Validation


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    @property
    def teams(self):
        return [self.red_bull_team, self.mercedes_team]

    def register_team_for_season(self, team_name: str, budget: int):
        Validation.item_duplicate(team_name, FormulaTeam.teams, "Invalid team name!")

        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        Validation.team_registered(self.teams, "Not all teams have registered for the season.")

        winner = self.red_bull_team.name if red_bull_pos < mercedes_pos else self.mercedes_team.name
        output = []

        for pos, team in zip([red_bull_pos, mercedes_pos], self.teams):
            output.append(f"{team.name}: {team.calculate_revenue_after_race(pos)}. ")
        output.append(f"{winner} is ahead at the {race_name} race.")

        return "".join(output)
