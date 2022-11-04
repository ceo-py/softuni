from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        if "Red Bull" != team_name != "Mercedes":
            raise ValueError("Invalid team name!")

        if "Red Bull" == team_name:
            self.red_bull_team = RedBullTeam(budget)

        elif "Mercedes" == team_name:
            self.mercedes_team = MercedesTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.mercedes_team is None or self.red_bull_team is None:
            raise Exception("Not all teams have registered for the season.")

        output = f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. "
        output += f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. "
        team_display = "Red Bull"
        if mercedes_pos < red_bull_pos:
            team_display = "Mercedes"

        output += f"{team_display} is ahead at the {race_name} race."
        return output
