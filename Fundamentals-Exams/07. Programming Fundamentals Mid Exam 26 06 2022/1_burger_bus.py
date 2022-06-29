number_of_cities = int(input())

total_profit = 0
for city in range(1, number_of_cities + 1):
    name_of_the_city = input()
    owners_income = float(input())
    owners_expenses = float(input())
    if city % 5 == 0:
        owners_income *= 0.90
    elif city % 3 == 0:
        owners_expenses *= 1.5
    current_profit = owners_income - owners_expenses
    total_profit += current_profit
    print(f"In {name_of_the_city} Burger Bus earned {current_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
