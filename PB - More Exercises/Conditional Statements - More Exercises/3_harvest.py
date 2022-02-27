import math

square_meters_vineyard = int(input())
square_meters_grapes = float(input())
liters_needed_wine = int(input())
workers = int(input())

vine_from_vineyard = 0.40
needed_grapes_for_liter_wine = 2.5
total_grapes = square_meters_vineyard * square_meters_grapes
wine = (vine_from_vineyard * total_grapes) / needed_grapes_for_liter_wine

if wine >= liters_needed_wine:
    left_wine = wine - liters_needed_wine
    litters_wine_per_person = left_wine / workers
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.\n{math.ceil(left_wine)} "
          f"liters left -> {math.ceil(litters_wine_per_person)} liters per person.")
else:
    wine = abs(wine - liters_needed_wine)
    print(f"It will be a tough winter! More {math.floor(wine)} liters wine needed.")
