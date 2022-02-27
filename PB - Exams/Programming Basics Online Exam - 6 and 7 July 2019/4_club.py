wanted_profit = float(input())

total_profit = 0
number_of_cocktails = 0
cocktail_price = 0
need_it_profit = 0
cocktail_total_price = 0

while True:

    cocktail_name = input()

    if cocktail_name == "Party!":
        need_it_profit = wanted_profit - total_profit
        print(f"We need {need_it_profit:.2f} leva more.\nClub income - {total_profit:.2f} leva.")
        break

    else:
        number_of_cocktails = int(input())
        cocktail_price = len(cocktail_name)
        cocktail_total_price = cocktail_price * number_of_cocktails

    if cocktail_total_price % 2 == 0:
        total_profit += cocktail_total_price

    else:
        total_profit += (cocktail_total_price - (cocktail_total_price * 0.25))

    if total_profit >= wanted_profit:
        print(f"Target acquired.\nClub income - {total_profit:.2f} leva.")
        break