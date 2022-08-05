number_of_heroes = int(input())

heroes_info = {}

for hero in range(number_of_heroes):
    hero_name, *info = (int(x) if x.isdigit() else x for x in input().split())
    heroes_info[hero_name] = info


def cast_spell(info):
    hero_name, mp_needed, spell_name = info
    if mp_needed > heroes_info[hero_name][1]:
        return f"{hero_name} does not have enough MP to cast {spell_name}!"
    heroes_info[hero_name][1] -= mp_needed
    return f"{hero_name} has successfully cast {spell_name} and now has {heroes_info[hero_name][1]} MP!"


def take_damage(info):
    hero_name, damage, attacker = info
    heroes_info[hero_name][0] -= damage
    if heroes_info[hero_name][0] > 0:
        return f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_info[hero_name][0]} HP left!"
    del heroes_info[hero_name]
    return f"{hero_name} has been killed by {attacker}!"


def heal(info):
    hero_name, amount = info
    if heroes_info[hero_name][0] + amount > 100:
        amount = 100 - heroes_info[hero_name][0]
    heroes_info[hero_name][0] += amount
    return f"{hero_name} healed for {amount} HP!"


def recharge(info):
    hero_name, amount = info
    if heroes_info[hero_name][1] + amount > 200:
        amount = 200 - heroes_info[hero_name][1]
    heroes_info[hero_name][1] += amount
    return f"{hero_name} recharged for {amount} MP!"


def show_result():
    for hero in heroes_info:
        print(f"{hero}\n  "
              f"HP: {heroes_info[hero][0]}\n  "
              f"MP: {heroes_info[hero][1]}")


command_func = {
"CastSpell" : cast_spell,
"TakeDamage": take_damage,
"Recharge" : recharge,
"Heal": heal
}

command = input()
while command != "End":
    command_type, *info = (int(x) if x.isdigit() else x for x in command.split(" - "))
    print(command_func[command_type](info))
    command = input()

show_result()





#
# number_heroes = int(input())
#
# heroes_info = {}
#
#
# class Heroes:
#     def __init__(self, name):
#         self.name = name
#         self.hp = 0
#         self.mp = 0
#
#     def add_hp(self, hp):
#         self.hp += hp
#
#     def add_mp(self, mp):
#         self.mp += mp
#
#     def cast_spall(self, mp_need, spell_name):
#         if self.mp >= mp_need:
#             self.mp -= mp_need
#             return f"{self.name} has successfully cast {spell_name} and now has {self.mp} MP!"
#         return f"{self.name} does not have enough MP to cast {spell_name}!"
#
#     def take_damage(self, damage, attacker):
#         self.hp -= damage
#         if self.hp > 0:
#             return f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!"
#         del heroes_info[self.name]
#         return f"{self.name} has been killed by {attacker}!"
#
#     def recharge(self, amount):
#         if self.mp + amount > 200:
#             amount = 200 - self.mp
#         self.mp += amount
#         return f"{self.name} recharged for {amount} MP!"
#
#     def heal(self, amount):
#         if self.hp + amount > 100:
#             amount = 100 - self.hp
#         self.hp += amount
#         return f"{self.name} healed for {amount} HP!"
#
#     def __repr__(self):
#         return f"{self.name}\n  " \
#                f"HP: {self.hp}\n  " \
#                f"MP: {self.mp}"
#
#
# for hero in range(number_heroes):
#     hero_name, hp, mp = [int(x) if x.isdigit() else x for x in input().split()]
#     heroes_info[hero_name] = heroes_info.get(hero_name, Heroes(hero_name))
#     heroes_info[hero_name].add_hp(hp)
#     heroes_info[hero_name].add_mp(mp)
#
# command = input()
#
# while command != "End":
#     command_type, hero_name, *info = [int(x) if x.isdigit() else x for x in command.split(" - ")]
#     if command_type == "Heal":
#         hp = info[0]
#         print(heroes_info[hero_name].heal(hp))
#     elif command_type == "Recharge":
#         mp = info[0]
#         print(heroes_info[hero_name].recharge(mp))
#     elif command_type == "TakeDamage":
#         damage, attacker = info
#         print(heroes_info[hero_name].take_damage(damage, attacker))
#     elif command_type == "CastSpell":
#         mp_need, spell_name = info
#         print(heroes_info[hero_name].cast_spall(mp_need, spell_name))
#
#     command = input()
#
# for hero in heroes_info.values():
#     print(hero)
#




# number_of_heroes = int(input())
#
# heroes_info = {}
#
# for hero in range(number_of_heroes):
#     hero_name, hp, mp = [int(x) if x.isdigit() else x for x in input().split()]
#     heroes_info[hero_name] = heroes_info.get(hero_name, {})
#     heroes_info[hero_name]["hp"] = hp
#     heroes_info[hero_name]["mp"] = mp
#
#
# def hero_cast_spell(hero_name, mp_needed, spell_name, heroes_info):
#     if heroes_info[hero_name]["mp"] >= mp_needed:
#         heroes_info[hero_name]["mp"] -= mp_needed
#         print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_info[hero_name]['mp']} MP!")
#     else:
#         print(f"{hero_name} does not have enough MP to cast {spell_name}!")
#     return heroes_info
#
#
# def hero_take_damage(hero_name, damage, attacker, heroes_info):
#     heroes_info[hero_name]["hp"] -= damage
#     if heroes_info[hero_name]["hp"] > 0:
#         print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_info[hero_name]['hp']} HP left!")
#     else:
#         del heroes_info[hero_name]
#         print(f"{hero_name} has been killed by {attacker}!")
#     return heroes_info
#
#
# def hero_recharge(hero_name, amount, heroes_info):
#     if heroes_info[hero_name]["mp"] + amount > 200:
#         amount = 200 - heroes_info[hero_name]["mp"]
#         heroes_info[hero_name]["mp"] = 200
#     else:
#         heroes_info[hero_name]["mp"] += amount
#     print(f"{hero_name} recharged for {amount} MP!")
#     return heroes_info
#
#
# def hero_heal(hero_name, amount, heroes_info):
#     if heroes_info[hero_name]["hp"] + amount > 100:
#         amount = 100 - heroes_info[hero_name]["hp"]
#         heroes_info[hero_name]["hp"] = 100
#     else:
#         heroes_info[hero_name]["hp"] += amount
#     print(f"{hero_name} healed for {amount} HP!")
#     return heroes_info
#
#
# def show_result():
#     for hero in heroes_info:
#         print(hero)
#         print(f"  HP: {heroes_info[hero]['hp']}")
#         print(f"  MP: {heroes_info[hero]['mp']}")
#
#
# command = input()
#
# while command != "End":
#     command, *info = [int(x) if x.isdigit() else x for x in command.split(" - ")]
#     if "Recharge" in command or "Heal" in command:
#         hero_name, amount = info
#         if "Heal" in command:
#             heroes_info = hero_heal(hero_name, amount, heroes_info)
#         elif "Recharge" in command:
#             heroes_info = hero_recharge(hero_name, amount, heroes_info)
#     elif "CastSpell" in command or "TakeDamage" in command:
#         hero_name, mp_needed_or_damage, spell_name_or_attacker = info
#         if "CastSpell" in command:
#             heroes_info = hero_cast_spell(hero_name, mp_needed_or_damage, spell_name_or_attacker, heroes_info)
#         elif "TakeDamage" in command:
#             heroes_info = hero_take_damage(hero_name, mp_needed_or_damage, spell_name_or_attacker, heroes_info)
#     command = input()
#
# show_result()




# number_of_heroes = int(input())
#
# heroes_info = {}
#
# for hero in range(number_of_heroes):
#     hero_name, hp, mp = [int(x) if x.isdigit() else x for x in input().split()]
#     heroes_info[hero_name] = heroes_info.get(hero_name, {})
#     heroes_info[hero_name]["hp"] = hp
#     heroes_info[hero_name]["mp"] = mp
#
#
# def hero_cast_spell(hero_name, mp_needed, spell_name, heroes_info):
#     if heroes_info[hero_name]["mp"] >= mp_needed:
#         heroes_info[hero_name]["mp"] -= mp_needed
#         print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_info[hero_name]['mp']} MP!")
#     else:
#         print(f"{hero_name} does not have enough MP to cast {spell_name}!")
#     return heroes_info
#
#
# def hero_take_damage(hero_name, damage, attacker, heroes_info):
#     heroes_info[hero_name]["hp"] -= damage
#     if heroes_info[hero_name]["hp"] > 0:
#         print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_info[hero_name]['hp']} HP left!")
#     else:
#         del heroes_info[hero_name]
#         print(f"{hero_name} has been killed by {attacker}!")
#     return heroes_info
#
#
# def hero_recharge(hero_name, amount, heroes_info):
#     if heroes_info[hero_name]["mp"] + amount > 200:
#         amount = 200 - heroes_info[hero_name]["mp"]
#         heroes_info[hero_name]["mp"] = 200
#     else:
#         heroes_info[hero_name]["mp"] += amount
#     print(f"{hero_name} recharged for {amount} MP!")
#     return heroes_info
#
#
# def hero_heal(hero_name, amount, heroes_info):
#     if heroes_info[hero_name]["hp"] + amount > 100:
#         amount = 100 - heroes_info[hero_name]["hp"]
#         heroes_info[hero_name]["hp"] = 100
#     else:
#         heroes_info[hero_name]["hp"] += amount
#     print(f"{hero_name} healed for {amount} HP!")
#     return heroes_info
#
#
# def show_result():
#     for hero in heroes_info:
#         print(hero)
#         print(f"  HP: {heroes_info[hero]['hp']}")
#         print(f"  MP: {heroes_info[hero]['mp']}")
#
#
# command = input()
#
# while command != "End":
#     if "Recharge" in command or "Heal" in command:
#         _, hero_name, amount = [int(x) if x.isdigit() else x for x in command.split(" - ")]
#         if "Heal" in command:
#             heroes_info = hero_heal(hero_name, amount, heroes_info)
#         elif "Recharge" in command:
#             heroes_info = hero_recharge(hero_name, amount, heroes_info)
#     elif "CastSpell" in command or "TakeDamage" in command:
#         _, hero_name, mp_needed_or_damage, spell_name_or_attacker = [int(x) if x.isdigit() else x for x in
#                                                                      command.split(" - ")]
#         if "CastSpell" in command:
#             heroes_info = hero_cast_spell(hero_name, mp_needed_or_damage, spell_name_or_attacker, heroes_info)
#         elif "TakeDamage" in command:
#             heroes_info = hero_take_damage(hero_name, mp_needed_or_damage, spell_name_or_attacker, heroes_info)
#     command = input()
#
# show_result()
#
#
#





#
#
#
# number_heroes_to_input = int(input())
# hero_info = {}
#
#
# class Hero:
#     def __init__(self, name, hp, mp):
#         self.name = name
#         self.hp = hp
#         self.mp = mp
#
#     def cast_spell(self, mp_needed, spell_name):
#         if self.mp >= mp_needed:
#             self.mp -= mp_needed
#             return f"{self.name} has successfully cast {spell_name} and now has {self.mp} MP!"
#         else:
#             return f"{self.name} does not have enough MP to cast {spell_name}!"
#
#     def take_damage(self, damage, attacker):
#         self.hp -= damage
#         if self.hp > 0:
#             return f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!"
#         else:
#             name_hero = self.name
#             del hero_info[self.name]
#             return f"{name_hero} has been killed by {attacker}!"
#
#     def recharge_hero(self, amount):
#         if self.mp + amount > 200:
#             result = 200 - self.mp
#             self.mp = 200
#             return f"{self.name} recharged for {result} MP!"
#
#         else:
#             self.mp += amount
#             return f"{self.name} recharged for {amount} MP!"
#
#     def heal(self, amount):
#         if self.hp + amount > 100:
#             result = 100 - self.hp
#             self.hp = 100
#             return f"{self.name} healed for {result} HP!"
#
#         else:
#             self.hp += amount
#             return f"{self.name} healed for {amount} HP!"
#
#     def __repr__(self):
#         return f"{self.name}\n  HP: {hero_info[name].hp}\n  MP: {hero_info[name].mp}"
#
#
# for _ in range(number_heroes_to_input):
#     hero_name, hero_hp, hero_mp = input().split()
#     hero_info[hero_name] = Hero(hero_name, int(hero_hp), int(hero_mp))
#
# command = input()
#
# while command != "End":
#     type_command, hero_name_, *info = command.split(" - ")
#     if type_command == "Heal":
#         print(hero_info[hero_name_].heal(int(info[0])))
#     elif type_command == "Recharge":
#         print(hero_info[hero_name_].recharge_hero(int(info[0])))
#     elif type_command == "TakeDamage":
#         print(hero_info[hero_name_].take_damage(int(info[0]), info[-1]))
#     elif type_command == "CastSpell":
#         print(hero_info[hero_name_].cast_spell(int(info[0]), info[-1]))
#     command = input()
#
# for name in hero_info:
#     print(hero_info[name])
#
#




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
