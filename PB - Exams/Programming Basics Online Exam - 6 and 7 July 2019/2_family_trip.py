budget = float(input())
number_nights = int(input())
night_price = float(input())
percent_expenses = int(input())

if number_nights > 7:

    # night_price = (night_price * 0.05) - number_nights
    night_price *= 0.95

total_price = night_price * number_nights
total_expenses = budget * (percent_expenses / 100)

total = total_price + total_expenses
difference = f'{abs(budget - total):.2f}'

if total <= budget:
    print(f'Ivanovi will be left with {difference} leva after vacation.')
else:
    print(f'{difference} leva needed.')











# budget = float(input())
# number_sleeps = int(input())
# price_per_sleep = float(input())
# other_expenses = int(input())
#
# other_expenses = ((other_expenses / 100) * budget)
#
# if number_sleeps > 7:
#     price_per_sleep += - price_per_sleep * 0.05
#
# total_price = price_per_sleep * number_sleeps
# total = other_expenses + total_price
# money_left = budget - total
#
# if money_left >= 0:
#     print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
#
# else:
#     print(f"{abs(money_left):.2f} leva needed.")
