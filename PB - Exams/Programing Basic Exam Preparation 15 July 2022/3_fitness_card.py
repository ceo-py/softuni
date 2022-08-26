budget = float(input())
sex = input()
age = int(input())
type_sport = input()


fitness_card_price = 0

if "f" == sex:
    if "Gym" == type_sport:
        fitness_card_price = 35
    elif "Boxing" == type_sport:
        fitness_card_price = 37
    elif "Yoga" == type_sport:
        fitness_card_price = 42
    elif "Zumba" == type_sport:
        fitness_card_price = 31
    elif "Dances" == type_sport:
        fitness_card_price = 53
    elif "Pilates" == type_sport:
        fitness_card_price = 37

elif "m" == sex:
    if "Gym" == type_sport:
        fitness_card_price = 42
    elif "Boxing" == type_sport:
        fitness_card_price = 41
    elif "Yoga" == type_sport:
        fitness_card_price = 45
    elif "Zumba" == type_sport:
        fitness_card_price = 34
    elif "Dances" == type_sport:
        fitness_card_price = 51
    elif "Pilates" == type_sport:
        fitness_card_price = 39


if 19 >= age:
    fitness_card_price *= 0.80

if fitness_card_price > budget:
    diffrence = abs(fitness_card_price - budget)
    print(f"You don't have enough money! You need ${diffrence:.2f} more.")
else:
    print(f"You purchased a 1 month pass for {type_sport}.")
