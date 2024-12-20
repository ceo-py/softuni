class SpaceCraft:
    def __init__(self):
        self.position = (0, 0)
        self.resources = 100
        self.spaceship_mark = "S"

    def refill_resources(self) -> None:
        self.resources += 10
        if self.resources > 100:
            self.resources = 100

    def make_move(self, resource: int):
        self.resources -= resource

    def new_position(self, position: tuple) -> None:
        self.position = position


class Game:
    def __init__(self, space_size: int, ship: SpaceCraft):
        self.space_field = []
        self.space_field_size = space_size
        self.ship = ship
        self.planet_b = "P"
        self.meteorites = "M"
        self.space_stations = "R"
        self.mission_status = ""

    def change_field_symbol(self, symbol: str, row: int, col: int) -> None:
        self.space_field[row][col] = symbol

    def get_space_craft_position(self, *position: tuple) -> None:
        self.ship.position = position
        self.change_field_symbol(".", *position)

    @staticmethod
    def get_direction(direction: str) -> tuple:
        return {
            "up": (-1, 0),
            "down": (1, 0),
            "right": (0, 1),
            "left": (0, -1),
        }.get(direction)

    def make_step(self, row: int, col: int) -> str:
        return self.space_field[row][col]

    def create_space_field(self) -> None:
        for row in range(self.space_field_size):
            self.space_field.append(list(input().split()))
            if self.ship.spaceship_mark not in self.space_field[row]:
                continue
            self.get_space_craft_position(
                row, self.space_field[row].index(self.ship.spaceship_mark)
            )

    def is_in_space_boundaries(self, row, col) -> bool:
        return 0 <= row < self.space_field_size and 0 <= col < self.space_field_size

    def targeted_position(self, changes: tuple) -> tuple:
        return tuple(
            self.ship.position[index_change] + changes[index_change]
            for index_change in range(2)
        )

    def __str__(self):
        output = [self.mission_status, *[" ".join(row) for row in self.space_field]]
        return "\n".join(output)


game_state = Game(int(input()), SpaceCraft())
game_state.create_space_field()

while game_state.ship.resources >= 5:
    game_state.ship.make_move(5)
    new_position = game_state.targeted_position(game_state.get_direction(input()))

    if not game_state.is_in_space_boundaries(*new_position):
        game_state.mission_status = "Mission failed! The spaceship was lost in space."
        game_state.change_field_symbol("S", *game_state.ship.position)
        break

    step_on = game_state.make_step(*new_position)
    game_state.ship.new_position(new_position)

    if game_state.space_stations == step_on:
        game_state.ship.refill_resources()

    elif game_state.meteorites == step_on:
        game_state.ship.make_move(5)
        game_state.change_field_symbol(".", *new_position)

    elif game_state.planet_b == step_on:
        game_state.mission_status = f"Mission accomplished! The spaceship reached Planet B with {game_state.ship.resources} resources left."
        break
else:
    game_state.mission_status = "Mission failed! The spaceship was stranded in space."
    game_state.change_field_symbol("S", *game_state.ship.position)

print(game_state)
