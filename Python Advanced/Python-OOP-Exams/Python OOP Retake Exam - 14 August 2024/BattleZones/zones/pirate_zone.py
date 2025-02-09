from project.zones.base_zone import BaseZone

class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, volume=self.INITIAL_VOLUME)

    def zone_info(self):
        royal_ships, pirate_ships = self.get_royal_and_pirate_ships()
        output = [
            "@Pirate Zone Statistics@",
            f"Code: {self.code}; Volume: {self.volume}",
            f"Battleships currently in the Pirate Zone: {len(self.ships)}, {len(royal_ships)} out of them are Royal Battleships.",
        ]
        if self.ships:
            output.append(f"#{(', ').join(ship.name for ship in self.get_ships())}#")
        
        return "\n".join(output)

