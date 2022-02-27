car_budget = float(input())
season = input()

if season == "Summer" and car_budget <= 100:
    total = car_budget * 0.35
    print(f"Economy class\nCabrio - {total:.2f}")
elif season == "Summer" and car_budget <= 500:
    total = car_budget * 0.45
    print(f"Compact class\nCabrio - {total:.2f}")
elif season == "Winter" and car_budget <= 100:
    total = car_budget * 0.65
    print(f"Economy class\nJeep - {total:.2f}")
elif season == "Winter" and car_budget <= 500:
    total = car_budget * 0.80
    print(f"Compact class\nJeep - {total:.2f}")
elif car_budget > 500:
    total = car_budget * 0.90
    print(f"Luxury class\nJeep - {total:.2f}")
