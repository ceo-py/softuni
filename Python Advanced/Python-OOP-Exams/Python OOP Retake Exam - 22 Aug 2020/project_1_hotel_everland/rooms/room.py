class Room:
    room_cost = 0

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def total_monthly_cost(self):
        return self.expenses + self.room_cost

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        self.expenses = sum(r.get_monthly_expense() for arg in args for r in arg)

    def __repr__(self):
        return f"{self.family_name} with {self.members_count} members. " \
               f"Budget: {self.budget:.2f}$, " \
               f"Expenses: {self.expenses:.2f}$\n" \
               f"--- Appliances monthly cost: {self.expenses:.2f}$"
