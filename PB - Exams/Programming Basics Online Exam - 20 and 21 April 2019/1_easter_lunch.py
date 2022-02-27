easter_cakes_numbers = int(input())
eggshells_numbers = int(input())
cookies_in_kg = int(input())

easter_cakes_toall = easter_cakes_numbers * 3.20
eggshells_total = eggshells_numbers * 4.35
cookies_total = cookies_in_kg * 5.40
paint_for_eggs = (eggshells_numbers * 12) * 0.15
total_price = easter_cakes_toall + eggshells_total + cookies_total + paint_for_eggs

print(f"{total_price:.2f}")
