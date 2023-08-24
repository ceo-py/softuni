target_income = float(input())

cocktail_name = input()
current_income = 0

while cocktail_name != 'Party!':
    cocktail_numbers = int(input())

    cocktail_price = len(cocktail_name)

    cocktail_total = cocktail_price * cocktail_numbers

    if cocktail_total % 2 != 0:
        cocktail_total *= 0.75

    current_income += cocktail_total

    if current_income >= target_income:
        print('Target acquired.')
        break

    cocktail_name = input()

else:
    print(f'We need {abs(current_income - target_income):.2f} leva more.')

print(f'Club income - {current_income:.2f} leva.')












# wanted_profit = float(input())
#
# total_profit = 0
# number_of_cocktails = 0
# cocktail_price = 0
# need_it_profit = 0
# cocktail_total_price = 0
#
# while True:
#
#     cocktail_name = input()
#
#     if cocktail_name == "Party!":
#         need_it_profit = wanted_profit - total_profit
#         print(f"We need {need_it_profit:.2f} leva more.\nClub income - {total_profit:.2f} leva.")
#         break
#
#     else:
#         number_of_cocktails = int(input())
#         cocktail_price = len(cocktail_name)
#         cocktail_total_price = cocktail_price * number_of_cocktails
#
#     if cocktail_total_price % 2 == 0:
#         total_profit += cocktail_total_price
#
#     else:
#         total_profit += (cocktail_total_price - (cocktail_total_price * 0.25))
#
#     if total_profit >= wanted_profit:
#         print(f"Target acquired.\nClub income - {total_profit:.2f} leva.")
#         break