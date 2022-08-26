minutes_walk_per_day = int(input())
number_walks_per_day = int(input())
taken_calories = int(input())

total_minutes_walk = minutes_walk_per_day * number_walks_per_day
total_burn_calories = total_minutes_walk * 5
target_burn_calories = taken_calories / 2

if total_burn_calories >= target_burn_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burn_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burn_calories}.")



