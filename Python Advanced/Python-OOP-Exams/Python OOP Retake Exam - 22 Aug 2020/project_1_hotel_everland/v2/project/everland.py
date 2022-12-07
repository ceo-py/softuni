class Everland:
    def __init__(self):
        self.rooms = []
        self.total_population = 0

    def add_room(self, room):
        self.rooms.append(room)
        self.total_population += room.members_count

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.get_monthly_expense()
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        output = []
        for r in self.rooms[:]:
            total_cost = r.expenses + r.room_cost
            if r.budget >= total_cost:
                r.budget -= total_cost
                output.append(f"{r.family_name} paid {total_cost:.2f}$ and have {r.budget:.2f}$ left.")
            else:
                output.append(f"{r.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(r)
                self.total_population -= r.members_count

        return "\n".join(output)

    def status(self):
        output = [f"Total population: {self.total_population}"]
        for r in self.rooms:
            output.append(
                f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$")
            for n, c in enumerate(r.children, 1):
                output.append(f"--- Child {n} monthly cost: {c.get_monthly_expense():.2f}$")
            output.append(f"--- Appliances monthly cost: {r.expenses:.2f}$")
        return "\n".join(output)
