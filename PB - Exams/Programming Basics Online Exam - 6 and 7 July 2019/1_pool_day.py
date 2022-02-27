import math

number_people = int(input())
entry_tax = float(input())
price_deck_chair = float(input())
price_umbrella = float(input())

total_entry_tax = number_people * entry_tax
deck_chair_money = math.ceil(number_people * 0.75) * price_deck_chair
umbrella_money = math.ceil(number_people / 2) * price_umbrella

total = total_entry_tax + deck_chair_money + umbrella_money

print(f"{total:.2f} lv.")
