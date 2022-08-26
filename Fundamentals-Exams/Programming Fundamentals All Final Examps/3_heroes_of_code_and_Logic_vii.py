number_heroes = int(input())

heroes_info = {}


class Heroes:
    def __init__(self, name):
        self.name = name
        self.hp = 0
        self.mp = 0

    def add_hp(self, hp):
        self.hp += hp

    def add_mp(self, mp):
        self.mp += mp

    def cast_spall(self, mp_need, spell_name):
        if self.mp >= mp_need:
            self.mp -= mp_need
            return f"{self.name} has successfully cast {spell_name} and now has {self.mp} MP!"
        return f"{self.name} does not have enough MP to cast {spell_name}!"

    def take_damage(self, damage, attacker):
        self.hp -= damage
        if self.hp > 0:
            return f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!"
        del heroes_info[self.name]
        return f"{self.name} has been killed by {attacker}!"

    def recharge(self, amount):
        if self.mp + amount > 200:
            amount = 200 - self.mp
        self.mp += amount
        return f"{self.name} recharged for {amount} MP!"

    def heal(self, amount):
        if self.hp + amount > 100:
            amount = 100 - self.hp
        self.hp += amount
        return f"{self.name} healed for {amount} HP!"

    def __repr__(self):
        return f"{self.name}\n  " \
               f"HP: {self.hp}\n  " \
               f"MP: {self.mp}"


for hero in range(number_heroes):
    hero_name, hp, mp = [int(x) if x.isdigit() else x for x in input().split()]
    heroes_info[hero_name] = heroes_info.get(hero_name, Heroes(hero_name))
    heroes_info[hero_name].add_hp(hp)
    heroes_info[hero_name].add_mp(mp)

command = input()

while command != "End":
    command_type, hero_name, *info = [int(x) if x.isdigit() else x for x in command.split(" - ")]
    if command_type == "Heal":
        hp = info[0]
        print(heroes_info[hero_name].heal(hp))
    elif command_type == "Recharge":
        mp = info[0]
        print(heroes_info[hero_name].recharge(mp))
    elif command_type == "TakeDamage":
        damage, attacker = info
        print(heroes_info[hero_name].take_damage(damage, attacker))
    elif command_type == "CastSpell":
        mp_need, spell_name = info
        print(heroes_info[hero_name].cast_spall(mp_need, spell_name))

    command = input()

for hero in heroes_info.values():
    print(hero)
