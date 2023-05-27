price_holiday = float(input())
puzzles = int(input())
speaking_toys = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

total_toys_amount = puzzles + speaking_toys + teddy_bears + minions + trucks

puzzle_price = 2.60
speaking_toy_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_price = puzzles * puzzle_price + speaking_toys * speaking_toy_price\
    + teddy_bears * teddy_bear_price + minions * minion_price + trucks * truck_price

if total_toys_amount >= 50:
    total_price = total_price * .75

rent = total_price * .10
profits = total_price - rent
money_left = profits - price_holiday

if profits >= price_holiday:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_left = price_holiday - profits
    print(f"Not enough money! {money_left:.2f} lv needed.")











#
# holiday_price = float(input())
# puzzels = int(input())
# talking_dols = int(input())
# tedy_bears = int(input())
# minions = int(input())
# trucks = int(input())
#
# magazine = {
#     "puzzels": 2.60,
#     "talking_dols": 3,
#     "tedy_bears": 4.10,
#     "minions": 8.20,
#     "trucks": 2,
#     "price_off": 0.25,
#     "rent": 0.10
# }
#
# toys_total_price = magazine["puzzels"] * puzzels + magazine["talking_dols"] * talking_dols + magazine[
#     "tedy_bears"] * tedy_bears \
#                    + magazine["minions"] * minions + magazine["trucks"] * trucks
# toys_count = puzzels + talking_dols + tedy_bears + minions + trucks
# if toys_count >= 50:
#     toys_total_price = toys_total_price - (toys_total_price * magazine["price_off"])
# magazine_rent = toys_total_price * magazine["rent"]
# magazine_winning = toys_total_price - magazine_rent
# if magazine_winning >= holiday_price:
#     magazine_winning += - holiday_price
#     print(f"Yes! {magazine_winning:.2f} lv left.")
# else:
#     magazine_winning = holiday_price - magazine_winning
#     print(f"Not enough money! {magazine_winning:.2f} lv needed.")


#
# vacation_price = float(input())
# puzzle = int(input())
# dolls = int(input())
# teddy = int(input())
# minions = int(input())
# truck = int(input())
#
# puzzle_price = puzzle * 2.60
# dolls_price = dolls * 3
# teddy_price = teddy * 4.10
# minions_price = minions * 8.20
# truck_price = truck * 2
#
# total_order_number = puzzle + dolls + teddy + minions + truck
# total_price = puzzle_price + dolls_price + teddy_price + minions_price + truck_price
#
# if total_order_number >= 50:
#     total_price = total_price - (total_price * 0.25)
#
# rent = total_price * 0.1
# final_amount = total_price - rent
# profit = abs(final_amount - vacation_price)
#
# if final_amount >= vacation_price:
#     print(f"Yes! {profit:.2f} lv left.")
# else:
#     print(f"Not enough money! {profit:.2f} lv needed.")
#
#


# trip_cost = float(input())
# number_of_puzzles = int(input())
# number_of_dolls = int(input())
# number_of_teddy_bears = int(input())
# number_of_minions = int(input())
# number_of_trucks = int(input())
#
# PUZZLE_PRICE = 2.60
# DOLL_PRICE = 3
# TEDDY_BEAR_PRICE = 4.10
# MINION_PRICE = 8.20
# TRUCK_PRICE = 2
#
# toys_price = (number_of_puzzles * PUZZLE_PRICE) + \
#              (number_of_dolls * DOLL_PRICE) + \
#              (number_of_teddy_bears * TEDDY_BEAR_PRICE) + \
#              (number_of_minions * MINION_PRICE) + \
#              (number_of_trucks * TRUCK_PRICE)
# toys_amount = number_of_puzzles + number_of_dolls + number_of_teddy_bears + \
#               number_of_minions + number_of_trucks
# if toys_amount >= 50:
#     toys_price = toys_price - (toys_price * 0.25)
#
# rent = toys_price * 0.10
# profit = toys_price - rent
# money_left = profit - trip_cost
#
# if profit >= trip_cost:
#     print(f"Yes! {money_left:.2f} lv left.")
# else:
#     money_needed = trip_cost - profit
#     print(f"Not enough money! {money_needed:.2f} lv needed.")
#
#