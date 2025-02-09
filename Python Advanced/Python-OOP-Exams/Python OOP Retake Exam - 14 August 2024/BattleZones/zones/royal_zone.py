from project.zones.base_zone import BaseZone

class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, volume=self.INITIAL_VOLUME)

    def zone_info(self):
        royal_ships, pirate_ships = self.get_royal_and_pirate_ships()
        output = [
            "@Royal Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Royal Zone: {len(self.ships)}, {len(pirate_ships)} out of them are Pirate Battleships.",
        ]
        if self.ships:
            output.append(f"#{(', ').join(ship.name for ship in self.get_ships())}#")

        return "\n".join(output)
