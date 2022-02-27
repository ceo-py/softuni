film_budget = float(input())
count_extras = int(input())
price_per_one_extra = float(input())

decorator_expenses = film_budget * 0.10
extras_over_onehundred_off = 0.10
if count_extras > 150:
    gear_for_extras = count_extras * price_per_one_extra
    gear_for_extras = gear_for_extras - (gear_for_extras * extras_over_onehundred_off)
else:
    gear_for_extras = count_extras * price_per_one_extra

gear_for_extras += decorator_expenses

if film_budget >= gear_for_extras:
    total_movie_cost = film_budget - gear_for_extras
    print(f"Action!\nWingard starts filming with {total_movie_cost:.2f} leva left.")
else:
    total_movie_cost = gear_for_extras - film_budget
    print(f"Not enough money!\nWingard needs {total_movie_cost:.2f} leva more.")
