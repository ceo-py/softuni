count_days = int(input())
total_food = float(input())
sum_food_eaten_by_dog = 0
sum_food_eaten_by_cat = 0
sum_biscuits = 0

for day in range(1, count_days + 1):
    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())

    if day % 3 == 0:
        sum_biscuits = sum_biscuits + (food_eaten_by_dog + food_eaten_by_cat) * 0.10
    sum_food_eaten_by_dog += food_eaten_by_dog
    sum_food_eaten_by_cat += food_eaten_by_cat

sum_all = sum_food_eaten_by_dog + sum_food_eaten_by_cat

percentage_eaten_food = (sum_all / total_food) * 100
percentage_eaten_from_dog = (sum_food_eaten_by_dog / sum_all) * 100
percentage_eaten_from_cat = (sum_food_eaten_by_cat / sum_all) * 100

print(f"Total eaten biscuits: {round(sum_biscuits)}gr.")
print(f"{percentage_eaten_food:.2f}% of the food has been eaten.")
print(f"{percentage_eaten_from_dog:.2f}% eaten from the dog.")
print(f"{percentage_eaten_from_cat:.2f}% eaten from the cat.")
