import math

number_days = int(input())
left_foot_inkg = int(input())
food_for_dog_per_kg = float(input())
food_for_cat_per_kg = float(input())
food_for_turtle_per_grams = float(input())

dog_food_needed = number_days * food_for_dog_per_kg
cat_food_needed = number_days * food_for_cat_per_kg
turtle_food_needed = (number_days * food_for_turtle_per_grams) / 1000

total_food = left_foot_inkg - (dog_food_needed + cat_food_needed + turtle_food_needed)

if total_food >= 0:
    print(f"{math.floor(total_food)} kilos of food left.")
else:
    print(f"{math.ceil(abs(total_food))} more kilos of food are needed.")
