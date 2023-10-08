cozunaci = int(input())
numbers_eggs = int(input())
cookies_kg = int(input())

cozunaci_price = 3.20
crust_12_eggs_price = 4.35
cookies_kg_price = 5.40
paint_eggs_price = 0.15

cozunaci_total = cozunaci * cozunaci_price
crust_12_eggs_total = crust_12_eggs_price * numbers_eggs
cookies_kg_total = cookies_kg_price * cookies_kg
paint_eggs_total = paint_eggs_price * numbers_eggs * 12
total = cozunaci_total + crust_12_eggs_total + cookies_kg_total + paint_eggs_total
print(f'{total:.2f}')






# easter_cakes_numbers = int(input())
# eggshells_numbers = int(input())
# cookies_in_kg = int(input())
#
# easter_cakes_toall = easter_cakes_numbers * 3.20
# eggshells_total = eggshells_numbers * 4.35
# cookies_total = cookies_in_kg * 5.40
# paint_for_eggs = (eggshells_numbers * 12) * 0.15
# total_price = easter_cakes_toall + eggshells_total + cookies_total + paint_for_eggs
#
# print(f"{total_price:.2f}")
