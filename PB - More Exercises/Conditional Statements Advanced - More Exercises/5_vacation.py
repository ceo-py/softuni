vacation_budget = float(input())
season = input()

if season == "Summer" and vacation_budget <= 1000:
    total = vacation_budget * 0.65
    print(f"Alaska - Camp - {total:.2f}")
elif season == "Summer" and vacation_budget <= 3000:
    total = vacation_budget * 0.80
    print(f"Alaska - Hut - {total:.2f}")
elif season == "Winter" and vacation_budget <= 1000:
    total = vacation_budget * 0.45
    print(f"Morocco - Camp - {total:.2f}")
elif season == "Winter" and vacation_budget <= 3000:
    total = vacation_budget * 0.60
    print(f"Morocco - Hut - {total:.2f}")
elif vacation_budget > 3000 and season == "Summer":
    total = vacation_budget * 0.90
    print(f"Alaska - Hotel - {total:.2f}")
else:
    total = vacation_budget * 0.90
    print(f"Morocco - Hotel - {total:.2f}")
