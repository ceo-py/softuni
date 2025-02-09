from project.utils.validation import Validation
from project.zones.base_zone import BaseZone
from project.zones.royal_zone import RoyalZone
from project.zones.pirate_zone import PirateZone
from project.battleships.royal_battleship import RoyalBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.base_battleship import BaseBattleship

class BattleManager:

    def __init__(self):
        self.zones = []
        self.ships = []

    def get_valid_zone_type(self, zone_type: str):
        return {
            "RoyalZone": RoyalZone,
            "PirateZone": PirateZone,
        }.get(zone_type)

    def get_valid_ship_type(self, ship_type: str):
        return {
            "RoyalBattleship": RoyalBattleship,
            "PirateBattleship": PirateBattleship,
        }.get(ship_type)

    def __find_object_by_attribute(self, text: str, attribute: str, collection: list) -> object:
        for obj in collection:
            if getattr(obj, attribute) == text:
                return obj

    def add_zone(self, zone_type: str, zone_code: str):
        found_zone = self.get_valid_zone_type(zone_type)

        if found_zone is None:
            raise Exception("Invalid zone type!")

        Validation.is_duplicate_by_attribute(zone_code, "code", self.zones, "Zone already exists!")

        new_zone = found_zone(zone_code)
        self.zones.append(new_zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        found_ship = self.get_valid_ship_type(ship_type)
        if found_ship is None:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        new_ship = found_ship(name, health, hit_strength)
        self.ships.append(new_ship)
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):

        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if ship in zone.ships:
            return f"Ship {ship.name} is already in {zone.code} zone!"

        ship_type = ship.__class__.__name__[:5]
        zone_type = zone.__class__.__name__[:5]

        if ship_type != zone_type:
            ship.is_attacking = False

        elif ship_type == zone_type:
            ship.is_attacking = True

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        found_ship = self.__find_object_by_attribute(ship_name, "name", self.ships)

        if not found_ship:
            return "No ship with this name!"

        if not found_ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(found_ship)
        return f"Successfully removed ship {ship_name}."


    def start_battle(self, zone: BaseZone):
        royal_ships, pirates_ships = zone.get_royal_and_pirate_ships()

        if len(royal_ships) == 0 or len(pirates_ships) == 0:
            return "Not enough participants. The battle is canceled."
        
        attacking_ship, defending_ship = (royal_ships, pirates_ships) if zone.__class__.__name__[:5] == "Royal" else (pirates_ships, royal_ships)
        most_powerful_ship = max(attacking_ship, key=lambda x: x.hit_strength)
        healthiest_enemy_ship = max(defending_ship, key=lambda x: x.health)

        most_powerful_ship.attack()
        healthiest_enemy_ship.take_damage(most_powerful_ship)

        if healthiest_enemy_ship.health <= 0:
            zone.ships.remove(healthiest_enemy_ship)
            self.ships.remove(healthiest_enemy_ship)
            return f"{healthiest_enemy_ship.name} lost the battle and was sunk."

        if most_powerful_ship.ammunition <= 0:
            zone.ships.remove(most_powerful_ship)
            self.ships.remove(most_powerful_ship)
            return f"{most_powerful_ship.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."


    def get_statistics(self):
        available_ships = [ship.name for ship in self.ships if ship.is_available]
        output = [
            f"Available Battleships: {len(available_ships)}",
            "***Zones Statistics:***",
            f"Total Zones: {len(self.zones)}",
            *[zone.zone_info() for zone in self.zones],
        ]

        if available_ships:
            output.insert(1, f"#{', '.join(available_ships)}#")

        return "\n".join(output)








# Initialize the BattleManager
battle_manager = BattleManager()

# Add zones
print(battle_manager.add_zone("RoyalZone", "001"))
print(battle_manager.add_zone("PirateZone", "002"))
print()

# Add battleships
print(battle_manager.add_battleship("RoyalBattleship", "RoyalOne", 50, 50))
print(battle_manager.add_battleship("RoyalBattleship", "RoyalTwo", 80, 45))
print(battle_manager.add_battleship("PirateBattleship", "PirateOne", 50, 50))
print(battle_manager.add_battleship("PirateBattleship", "PirateTwo", 70, 60))
print(battle_manager.add_battleship("RoyalBattleship", "RoyalThree", 100, 100))
print(battle_manager.add_battleship("PirateBattleship", "PirateThree", 90, 90))
print()

# Retrieve battleships and zones
royal_zone = battle_manager.zones[0]
pirate_zone = battle_manager.zones[1]

royal_one = battle_manager.ships[0]
royal_two = battle_manager.ships[1]
pirate_one = battle_manager.ships[2]
pirate_two = battle_manager.ships[3]

# Add ships to zones
print(battle_manager.add_ship_to_zone(royal_zone, royal_one))
print(battle_manager.add_ship_to_zone(royal_zone, pirate_one))
print(battle_manager.add_ship_to_zone(pirate_zone, royal_two))
print(battle_manager.add_ship_to_zone(pirate_zone, pirate_two))
print()

# Remove a battleship
print(battle_manager.remove_battleship("RoyalTwo"))
print(battle_manager.remove_battleship("Nonexistent"))
print()

# Start battle in RoyalZone
print(battle_manager.start_battle(royal_zone))
print()

# Start battle in PirateZone
print(battle_manager.start_battle(pirate_zone))
print()

# Start another battle in RoyalZone
print(battle_manager.start_battle(royal_zone))
print()

# Retrieve updated statistics
print(battle_manager.get_statistics())
print()

# Remove a battleship
print(battle_manager.remove_battleship("RoyalThree"))
