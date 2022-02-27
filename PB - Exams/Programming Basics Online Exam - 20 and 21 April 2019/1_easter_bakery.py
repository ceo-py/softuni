flour_price_per_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggshell_numbers = int(input())
yeast_kg = int(input())

sugar_price = flour_price_per_kg * 0.75
eggs_price = flour_price_per_kg * 1.1
yeast_price = sugar_price * 0.2
flour_total = flour_price_per_kg * flour_kg
sugar_total = sugar_price * sugar_kg
eggs_total = eggs_price * eggshell_numbers
yeast_total = yeast_price * yeast_kg
total = flour_total + sugar_total + eggs_total + yeast_total

print(f"{total:.2f}")
