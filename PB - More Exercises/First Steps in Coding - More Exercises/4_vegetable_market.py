vegetables_price_per_kg = float(input())
fruits_price_per_kg = float(input())
total_vegetables = float(input())
total_fruits = float(input())

total_price = ((vegetables_price_per_kg * total_vegetables) + (fruits_price_per_kg * total_fruits)) / 1.94

print(f"{total_price:.2f}")



# price_for_kg_vegetables = float(input())
# price_for_kg_fruits = float(input())
# obshto_vegetables_kg = int(input())
# obshto_fruits_kg = int(input())
#
# euro = 1.94
#
# prihodi = (price_for_kg_vegetables * obshto_vegetables_kg) + (price_for_kg_fruits * obshto_fruits_kg)
# income = prihodi / euro
#
# print(f"{income:.2f}")