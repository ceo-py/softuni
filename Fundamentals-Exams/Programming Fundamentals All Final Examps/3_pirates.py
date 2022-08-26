towns_info = {}


class Town:
    def __init__(self, name):
        self.name = name
        self.population = 0
        self.gold = 0

    def add_people(self, people):
        self.population += people

    def add_gold(self, gold):
        self.gold += gold

    def plunder(self, people, gold):
        self.population -= people
        self.gold -= gold
        print(f"{self.name} plundered! {gold} gold stolen, {people} citizens killed.")
        if self.population <= 0 or self.gold <= 0:
            del towns_info[self.name]
            print(f"{self.name} has been wiped off the map!")

    def prosper(self, gold):
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            self.gold += gold
            print(f"{gold} gold added to the city treasury. {self.name} now has {self.gold} gold.")

    def __repr__(self):
        return f"{self.name} -> Population: {self.population} citizens, Gold: {self.gold} kg"


command = input()

while command != "Sail":
    town, people, gold = [int(x) if x.isdigit() else x for x in command.split("||")]
    towns_info[town] = towns_info.get(town, Town(town))
    towns_info[town].add_gold(gold)
    towns_info[town].add_people(people)
    command = input()

command = input()
while command != "End":
    command_type, town_name, *info = [int(x) if x.isdigit() else x for x in command.split("=>")]
    if command_type == "Plunder":
        people, gold = info
        towns_info[town_name].plunder(people, gold)
    elif command_type == "Prosper":
        gold = int(info[0])
        towns_info[town_name].prosper(gold)
    command = input()

if towns_info:
    print(f"Ahoy, Captain! There are {len(towns_info.keys())} wealthy settlements to go to:")
    for town in towns_info.values():
        print(town)
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
