import math

number_days = int(input())
left_foot_inkg = int(input())
food_for_dog_per_kg = float(input())
food_for_cat_per_kg = float(input())
food_for_turtle_per_grams = float(input())

dog_food_needed = number_days * food_for_dog_per_kg
cat_food_needed = number_days * food_for_cat_per_kg
turtle_food_needed = (number_days * food_for_turtle_per_grams) / 1000

total_food = dog_food_needed + cat_food_needed + turtle_food_needed

food_left = left_foot_inkg - total_food

if total_food <= left_foot_inkg:
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    total_food = total_food - left_foot_inkg
    print(f"{math.ceil(total_food)} more kilos of food are needed.")
