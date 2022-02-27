movie_budget = float(input())
extras = int(input())
extras_clothing_price = float(input())

decor = movie_budget * 0.10

if extras > 150:
    extras_clothing_total = (extras_clothing_price * extras) - ((extras_clothing_price * extras) * 0.10)

else:
    extras_clothing_total = extras_clothing_price * extras

total_movie_cost = movie_budget - (decor + extras_clothing_total)

if movie_budget > total_movie_cost and total_movie_cost >= 0:
    print(f"Action!\nWingard starts filming with {total_movie_cost:.2f} leva left.")

else:
    print(f"Not enough money!\nWingard needs {abs(total_movie_cost):.2f} leva more.")
