budget = float(input())
number_sleeps = int(input())
price_per_sleep = float(input())
other_expenses = int(input())

other_expenses = ((other_expenses / 100) * budget)

if number_sleeps > 7:
    price_per_sleep += - price_per_sleep * 0.05

total_price = price_per_sleep * number_sleeps
total = other_expenses + total_price
money_left = budget - total

if money_left >= 0:
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")

else:
    print(f"{abs(money_left):.2f} leva needed.")
