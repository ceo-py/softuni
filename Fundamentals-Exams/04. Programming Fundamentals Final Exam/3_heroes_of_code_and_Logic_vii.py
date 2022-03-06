number_heroes = int(input())

hp = "hp"
mp = "mp"
hero_info = {}


def cast_spell(hero_name, mp_needed, spell_name):
    if hero_info[hero_name][mp] >= mp_needed:
        hero_info[hero_name][mp] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {hero_info[hero_name][mp]} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(hero_name, damage, attacker):
    hero_info[hero_name][hp] -= damage
    if hero_info[hero_name][hp] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_info[hero_name][hp]} HP left!")
    else:
        print(f"{hero_name} has been killed by {attacker}!")
        del hero_info[hero_name]


def recharge_hero(hero_name, amount):
    if (hero_info[hero_name][mp] + amount) > 200:
        print(f"{hero_name} recharged for {200 - hero_info[hero_name][mp]} MP!")
        hero_info[hero_name][mp] = 200
    else:
        print(f"{hero_name} recharged for {amount} MP!")
        hero_info[hero_name][mp] += amount


def heal_hero(hero_name, amount):
    if (hero_info[hero_name][hp] + amount) > 100:
        print(f"{hero_name} healed for {100 - hero_info[hero_name][hp]} HP!")
        hero_info[hero_name][hp] = 100
    else:
        hero_info[hero_name][hp] += amount
        print(f"{hero_name} healed for {amount} HP!")


def show_result():
    for hero in hero_info:
        print(f"{hero}\n  HP: {hero_info[hero][hp]}\n  MP: {hero_info[hero][mp]}")


def add_heroes():
    for _ in range(number_heroes):
        command = input().split()
        hero_name = command[0]
        hero_hp = int(command[1])
        hero_mp = int(command[-1])
        hero_info[hero_name] = {}
        hero_info[hero_name][hp] = hero_hp
        hero_info[hero_name][mp] = hero_mp


add_heroes()
command = input()

while command != "End":
    command = command.split(" - ")
    type_command = command[0]
    hero_name = command[1]
    hero_damage = int(command[2])
    if type_command == "Heal":
        heal_hero(hero_name, hero_damage)
    elif type_command == "Recharge":
        recharge_hero(hero_name, hero_damage)
    elif type_command == "TakeDamage":
        take_damage(hero_name, hero_damage, command[-1])
    elif type_command == "CastSpell":
        cast_spell(hero_name, hero_damage, command[-1])

    command = input()

show_result()
