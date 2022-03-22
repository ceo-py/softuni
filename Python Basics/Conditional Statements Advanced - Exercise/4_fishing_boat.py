group_budget = int(input())
season = input()
fisherman_count = int(input())
tariffs = {"season type": {"Summer": 4200, "Autumn": 4200, "Winter": 2600, "Spring": 3000},
           "price": {0.90: [fisherman_count <= 6], 0.85: [fisherman_count <= 11], 0.75: [fisherman_count >= 12],
                     "discount": [fisherman_count % 2 == 0 and season != "Autumn"]},
           "Off": {"[True]": 0.95, "[False]": 1}}

for key, value in tariffs["price"].items():
    if any(value):
        total_price = (tariffs["season type"][season] * key) * tariffs["Off"][str(tariffs["price"]["discount"])]
        break

left_over = abs(group_budget - total_price)
if group_budget >= total_price:
    print(f"Yes! You have {left_over:.2f} leva left.")
else:
    print(f"Not enough money! You need {left_over:.2f} leva.")


## reshenie samo s cenata v rechnik

# group_budget = int(input())
# season = input()
# fisherman_count = int(input())
#
# price = 0
# total_price =0
# tariffs = {
#         "Summer": 4200,
#         "Autumn": 4200,
#         "Winter": 2600,
#         "Spring": 3000,
# }
# if fisherman_count <= 6:
#     price = tariffs[season] * 0.90
#
# elif fisherman_count <= 11:
#     price = tariffs[season] * 0.85
#
# elif fisherman_count >= 12:
#     price = tariffs[season] * 0.75
#
# if fisherman_count % 2 == 0 and season != "Autumn":
#     price = price * 0.95
#
# left_over = abs(group_budget - price)
# if group_budget >= price:
#     print(f"Yes! You have {left_over:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {left_over:.2f} leva.")


## reshenie bez rechnik


# budget = int(input())
# season = str(input()).lower()
# fisherman = int(input())
#
# boat_price = 0
# boat_price_with_discount = 0
# 
# if season == "spring":
#     boat_price = 3000
# elif season == "summer" or season == "autumn":
#     boat_price = 4200
# else:
#     boat_price = 2600
#
# if fisherman <= 6:
#     boat_price_with_discount = boat_price * .9
# elif fisherman >= 12:
#     boat_price_with_discount = boat_price * .75
# else:
#     boat_price_with_discount = boat_price * .85
#
# if (fisherman % 2 == 0 and season != "autumn"):
#     boat_price_with_discount *= .95
#
# diff = budget - boat_price_with_discount
#
# if diff >= 0:
#     print(f"Yes! You have {diff:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {((-1) * diff):.2f} leva.")

