from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def total_population(self):
        return sum(r.members_count for r in self.rooms)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        return f"Monthly consumption: {sum(room.total_monthly_cost for room in self.rooms):.2f}$."

    def pay(self):
        output = []
        for r in self.rooms:
            if r.total_monthly_cost > r.budget:
                self.rooms.remove(r)
                output.append(f"{r.family_name} does not have enough budget and must leave the hotel.")
            else:
                r.budget -= r.total_monthly_cost
                output.append(f"{r.family_name} paid {r.total_monthly_cost}$ and have {r.budget}$ left.")

        return "\n".join(output)

    def status(self):
        return f"Total population: {self.total_population()}\n" + \
               "\n".join(room.__repr__() for room in self.rooms)
