from math import ceil

people_number = int(input())
tax = float(input())
sleeping_bed = float(input())
unbrela = float(input())


total_taxes = people_number * tax
unbrelas_total_price = ceil(people_number / 2) * unbrela
sleeping_bed_total_price = ceil(people_number * 0.75) * sleeping_bed

total = total_taxes + unbrelas_total_price + sleeping_bed_total_price

print(f'{total:.2f} lv.')






# import math
#
# number_people = int(input())
# entry_tax = float(input())
# price_deck_chair = float(input())
# price_umbrella = float(input())
#
# total_entry_tax = number_people * entry_tax
# deck_chair_money = math.ceil(number_people * 0.75) * price_deck_chair
# umbrella_money = math.ceil(number_people / 2) * price_umbrella
#
# total = total_entry_tax + deck_chair_money + umbrella_money
#
# print(f"{total:.2f} lv.")
