number_days = int(input())
total_food = float(input())

biscuits = 0
eat_food_dog = 0
eat_food_cat = 0

for day in range(1, number_days + 1):
    current_dog_food = int(input())
    current_cat_food = int(input())
    eat_food_dog += current_dog_food
    eat_food_cat += current_cat_food

    if day % 3 == 0:
        biscuits += (current_dog_food + current_cat_food) * 0.10

food_for_all_days = eat_food_dog + eat_food_cat
percent_food = (food_for_all_days / total_food) * 100
percent_dog_food = (eat_food_dog / food_for_all_days) * 100
percent_cat_food = (eat_food_cat / food_for_all_days) * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{percent_food:.2f}% of the food has been eaten.")
print(f"{percent_dog_food:.2f}% eaten from the dog.")
print(f"{percent_cat_food:.2f}% eaten from the cat.")
