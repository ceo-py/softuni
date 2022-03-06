food_kg, hay_kg, cover_kg, weight_kg = float(input()), float(input()), float(input()), float(input())

convert_rate = 1_000
food_kg *= convert_rate
hay_kg *= convert_rate
cover_kg *= convert_rate
weight_kg *= convert_rate / 3
enough_food = True
for day in range(1, 31):
    food_kg += - 300
    if day % 2 == 0:
        hay_kg += - food_kg * 0.05
    if day % 3 == 0:
        cover_kg += -weight_kg
    if all([food_kg > 0.00, hay_kg > 0.00, cover_kg > 0.00]):
        continue
    else:
        enough_food = False
        break

if enough_food:
    print(f"Everything is fine! Puppy is happy! Food: {(food_kg/convert_rate):.2f}, "
          f"Hay: {(hay_kg/convert_rate):.2f}, Cover: {(cover_kg/convert_rate):.2f}.")
else:
    print("Merry must go to the pet store!")
