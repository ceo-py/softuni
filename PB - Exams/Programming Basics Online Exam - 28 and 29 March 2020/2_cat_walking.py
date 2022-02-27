min_walk = int(input())
count_walks = int(input())
cat_calories = int(input())

calories_per_minute = 5
total_walks_minutes = count_walks * min_walk
calories_burn = total_walks_minutes * calories_per_minute
target_calories = cat_calories / 2

if calories_burn >= target_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burn}.")

else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burn}.")
