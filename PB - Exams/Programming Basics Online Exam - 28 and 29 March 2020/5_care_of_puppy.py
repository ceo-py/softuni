food_kg = int(input())

food = 0
while True:
    eated_food = (input())
    if eated_food == "Adopted":
        break
    food += int(eated_food)

total_buy_food = food_kg * 1000

if total_buy_food >= food:
    total = total_buy_food - food
    print(f"Food is enough! Leftovers: {total} grams.")

else:
    total = food - total_buy_food
    print(f"Food is not enough. You need {total} grams more.")