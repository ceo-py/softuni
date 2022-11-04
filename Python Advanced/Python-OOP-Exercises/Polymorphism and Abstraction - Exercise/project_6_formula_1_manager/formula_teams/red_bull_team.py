from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def __init__(self, budget: int):
        self.budget = budget
        self.sponsors = {
            1: 1_520_000,
            2: 820_000,
            3: 20_000,
            4: 20_000,
            5: 20_000,
            6: 20_000,
            7: 20_000,
            8: 20_000,
            9: 10_000,
            10: 10_000
        }
        self.expenses = 250_000


