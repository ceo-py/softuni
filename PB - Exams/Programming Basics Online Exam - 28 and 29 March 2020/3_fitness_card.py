availabe_money = float(input())
sex = input()
age = int(input())
sport = input()

male = {
    "Gym": 42,
    "Boxing": 41,
    "Yoga": 45,
    "Zumba": 34,
    "Dances": 51,
    "Pilates": 39
}

female = {
    "Gym": 35,
    "Boxing": 37,
    "Yoga": 42,
    "Zumba": 31,
    "Dances": 53,
    "Pilates": 37
}

if age <= 19:
    if "f" in sex:
        card_off = female[sport] - female[sport] * 0.20

        if availabe_money >= card_off:
            card_result = f"You purchased a 1 month pass for {sport}."

        else:
            money_needed = card_off - availabe_money
            card_result = f"You don't have enough money! You need ${money_needed:.2f} more."

    if "m" in sex:
        card_off = male[sport] - male[sport] * 0.20

        if availabe_money >= card_off:
            card_result = f"You purchased a 1 month pass for {sport}."

        else:
            money_needed = card_off - availabe_money
            card_result = f"You don't have enough money! You need ${money_needed:.2f} more."

elif "f" in sex:

    if availabe_money >= female[sport]:
        card_result = f"You purchased a 1 month pass for {sport}."

    else:
        money_needed = female[sport] - availabe_money
        card_result = f"You don't have enough money! You need ${money_needed:.2f} more."

elif "m" in sex:

    if availabe_money >= male[sport]:

        card_result = f"You purchased a 1 month pass for {sport}."

    else:
        money_needed = male[sport] - availabe_money
        card_result = f"You don't have enough money! You need ${money_needed:.2f} more."

print(card_result)
