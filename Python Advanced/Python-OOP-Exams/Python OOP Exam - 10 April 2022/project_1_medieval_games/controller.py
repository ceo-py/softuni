from project.validation.validation import Validation


class Controller:

    def __init__(self):

        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for p in players:
            if p not in self.players:
                added_players.append(p.name)
                self.players.append(p)

        return f"Successfully added: {', '.join(added_players)}"

    def __find_player(self, name: str):
        for p in self.players:
            if name == p.name:
                return p

    def __find_supply(self, name):
        return [(pos, s) for pos, s in enumerate(self.supplies) if s.__class__.__name__ == name][-1]

    @staticmethod
    def __duel(attacking_player: object, defending_player: object):
        if defending_player.stamina - attacking_player.stamina / 2 < 0:
            defending_player.stamina = 0
            return attacking_player.name
        defending_player.stamina -= attacking_player.stamina / 2

    def add_supply(self, *supplies):
        [self.supplies.append(s) for s in supplies]

    def sustain(self, player_name: str, sustenance_type: str):
        if all(p.name != player_name for p in self.players) or sustenance_type not in ("Food", "Drink"):
            return

        player = self.__find_player(player_name)
        if player.stamina == 100:
            return f"{player.name} have enough stamina."

        if sustenance_type == "Food":
            Validation.player_no_food_left(sustenance_type, self.supplies)
        elif sustenance_type == "Drink":
            Validation.player_no_drink_left(sustenance_type, self.supplies)

        pos, supply = self.__find_supply(sustenance_type)

        if player.stamina + supply.energy > 100:
            supply.energy = 100 - player.stamina

        player.stamina += supply.energy
        del self.supplies[pos]
        return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        p_one = self.__find_player(first_player_name)
        p_two = self.__find_player(second_player_name)

        zero_stamina = [f"Player {p.name} does not have enough stamina." for p in (p_one, p_two) if p.stamina == 0]
        if zero_stamina:
            return "\n".join(zero_stamina)

        player_duel = [p for p in sorted([p_one, p_two], key=lambda x: x.stamina)]
        r_one = self.__duel(*player_duel)
        if r_one:
            return f"Winner: {r_one}"

        r_two = self.__duel(*player_duel[::-1])
        if r_two:
            return f"Winner: {r_two}"

        winner = [p for p in sorted([p_one, p_two], key=lambda x: -x.stamina)][0]
        return f"Winner: {winner.name}"

    def next_day(self):
        for p in self.players:
            age = p.age * 2
            if p.stamina - age < 0:
                p.stamina = 0
            else:
                p.stamina -= age

        for p in self.players:
            for feeding in ("Food", "Drink"):
                self.sustain(p.name, feeding)

    def __str__(self):
        output = []
        for p in self.players:
            output.append(str(p))
        for s in self.supplies:
            output.append(s.details())
        return "\n".join(output)
