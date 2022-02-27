movie_budget = float(input())
movie_destination = input()
season = input()
number_days = int(input())

price = 0
money_left = 0

if "Dubai" == movie_destination and season == "Winter":
    price += 45_000

elif "Dubai" == movie_destination and season == "Summer":
    price += 40_000

elif "Sofia" == movie_destination and season == "Summer":
    price += 12_500

elif "Sofia" == movie_destination and season == "Winter":
    price += 17_000

elif "London" == movie_destination and season == "Winter":
    price += 24_000

elif "London" == movie_destination and season == "Summer":
    price += 20_250

if "Dubai" == movie_destination:
    price = price - (price * 0.30)

elif "Sofia" == movie_destination:
    price = price + (price * 0.25)

total = price * number_days
money_left = movie_budget - total
if movie_budget >= total:
    print(f"The budget for the movie is enough! We have {money_left:.2f} leva left!")

else:
    print(f"The director needs {abs(money_left):.2f} leva more!")
