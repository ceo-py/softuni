number_heroes_to_input = int(input())
hero_info = {}


class Hero:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    def cast_spell(self, mp_needed, spell_name):
        if self.mp >= mp_needed:
            self.mp -= mp_needed
            return f"{self.name} has successfully cast {spell_name} and now has {self.mp} MP!"
        else:
            return f"{self.name} does not have enough MP to cast {spell_name}!"

    def take_damage(self, damage, attacker):
        self.hp -= damage
        if self.hp > 0:
            return f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!"
        else:
            name_hero = self.name
            del hero_info[self.name]
            return f"{name_hero} has been killed by {attacker}!"

    def recharge_hero(self, amount):
        if self.mp + amount > 200:
            result = 200 - self.mp
            self.mp = 200
            return f"{self.name} recharged for {result} MP!"

        else:
            self.mp += amount
            return f"{self.name} recharged for {amount} MP!"

    def heal(self, amount):
        if self.hp + amount > 100:
            result = 100 - self.hp
            self.hp = 100
            return f"{self.name} healed for {result} HP!"

        else:
            self.hp += amount
            return f"{self.name} healed for {amount} HP!"

    def __repr__(self):
        return f"{self.name}\n  HP: {hero_info[name].hp}\n  MP: {hero_info[name].mp}"


for _ in range(number_heroes_to_input):
    hero_name, hero_hp, hero_mp = input().split()
    hero_info[hero_name] = Hero(hero_name, int(hero_hp), int(hero_mp))

command = input()

while command != "End":
    type_command, hero_name_, *info = command.split(" - ")
    if type_command == "Heal":
        print(hero_info[hero_name_].heal(int(info[0])))
    elif type_command == "Recharge":
        print(hero_info[hero_name_].recharge_hero(int(info[0])))
    elif type_command == "TakeDamage":
        print(hero_info[hero_name_].take_damage(int(info[0]), info[-1]))
    elif type_command == "CastSpell":
        print(hero_info[hero_name_].cast_spell(int(info[0]), info[-1]))
    command = input()

for name in hero_info:
    print(hero_info[name])






# no oop
# number_heroes = int(input())
#
# hp = "hp"
# mp = "mp"
# hero_info = {}
#
#
# def cast_spell(hero_name, mp_needed, spell_name):
#     if hero_info[hero_name][mp] >= mp_needed:
#         hero_info[hero_name][mp] -= mp_needed
#         print(f"{hero_name} has successfully cast {spell_name} and now has {hero_info[hero_name][mp]} MP!")
#     else:
#         print(f"{hero_name} does not have enough MP to cast {spell_name}!")
#
#
# def take_damage(hero_name, damage, attacker):
#     hero_info[hero_name][hp] -= damage
#     if hero_info[hero_name][hp] > 0:
#         print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_info[hero_name][hp]} HP left!")
#     else:
#         print(f"{hero_name} has been killed by {attacker}!")
#         del hero_info[hero_name]
#
#
# def recharge_hero(hero_name, amount):
#     if (hero_info[hero_name][mp] + amount) > 200:
#         print(f"{hero_name} recharged for {200 - hero_info[hero_name][mp]} MP!")
#         hero_info[hero_name][mp] = 200
#     else:
#         print(f"{hero_name} recharged for {amount} MP!")
#         hero_info[hero_name][mp] += amount
#
#
# def heal_hero(hero_name, amount):
#     if (hero_info[hero_name][hp] + amount) > 100:
#         print(f"{hero_name} healed for {100 - hero_info[hero_name][hp]} HP!")
#         hero_info[hero_name][hp] = 100
#     else:
#         hero_info[hero_name][hp] += amount
#         print(f"{hero_name} healed for {amount} HP!")
#
#
# def show_result():
#     for hero in hero_info:
#         print(f"{hero}\n  HP: {hero_info[hero][hp]}\n  MP: {hero_info[hero][mp]}")
#
#
# def add_heroes():
#     for _ in range(number_heroes):
#         command = input().split()
#         hero_name = command[0]
#         hero_hp = int(command[1])
#         hero_mp = int(command[-1])
#         hero_info[hero_name] = {}
#         hero_info[hero_name][hp] = hero_hp
#         hero_info[hero_name][mp] = hero_mp
#
#
# add_heroes()
# command = input()
#
# while command != "End":
#     command = command.split(" - ")
#     type_command = command[0]
#     hero_name = command[1]
#     hero_damage = int(command[2])
#     if type_command == "Heal":
#         heal_hero(hero_name, hero_damage)
#     elif type_command == "Recharge":
#         recharge_hero(hero_name, hero_damage)
#     elif type_command == "TakeDamage":
#         take_damage(hero_name, hero_damage, command[-1])
#     elif type_command == "CastSpell":
#         cast_spell(hero_name, hero_damage, command[-1])
#
#     command = input()
#
# show_result()
