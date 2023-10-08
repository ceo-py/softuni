flour_kilogram = float(input())
flour_kilograms = float(input())
sugar_kilograms = float(input())
eggshells_number = int(input())
yeast_packets = int(input())

sugar_kg_price = flour_kilogram * 0.75
eggshells_price = flour_kilogram * 1.10
yeast_price = sugar_kg_price * 0.20

flour_total_sum = flour_kilogram * flour_kilograms
sugar_total_sum = sugar_kg_price * sugar_kilograms
eggshells_sum = eggshells_price * eggshells_number
yeast_sum = yeast_price * yeast_packets

total_price = flour_total_sum + sugar_total_sum + eggshells_sum + yeast_sum
print(f'{total_price:.2f}')






#
# flour_price_per_kg = float(input())
# flour_kg = float(input())
# sugar_kg = float(input())
# eggshell_numbers = int(input())
# yeast_kg = int(input())
#
# sugar_price = flour_price_per_kg * 0.75
# eggs_price = flour_price_per_kg * 1.1
# yeast_price = sugar_price * 0.2
# flour_total = flour_price_per_kg * flour_kg
# sugar_total = sugar_price * sugar_kg
# eggs_total = eggs_price * eggshell_numbers
# yeast_total = yeast_price * yeast_kg
# total = flour_total + sugar_total + eggs_total + yeast_total
#
# print(f"{total:.2f}")
