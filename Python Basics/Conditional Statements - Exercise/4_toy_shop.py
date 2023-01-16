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
