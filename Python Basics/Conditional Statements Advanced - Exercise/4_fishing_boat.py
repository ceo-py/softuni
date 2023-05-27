budget = int(input())
season = input()
fishers = int(input())

total_price = 0

if season == "Spring":
    total_price = 3000
elif season == "Winter":
    total_price = 2600
else:
    total_price = 4200

if fishers <= 6:
    total_price *= 0.90
elif 7 <= fishers <= 11:
    total_price *= 0.85
else:
    total_price *= 0.75

if fishers % 2 == 0 and season != "Autumn":
    total_price *= 0.95

if total_price <= budget:
    print(f"Yes! You have {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva.")




# group_budget = int(input())
# season = input()
# fisherman_count = int(input())
# tariffs = {"season type": {"Summer": 4200, "Autumn": 4200, "Winter": 2600, "Spring": 3000},
#            "price": {0.90: [fisherman_count <= 6], 0.85: [fisherman_count <= 11], 0.75: [fisherman_count >= 12],
#                      "discount": [fisherman_count % 2 == 0 and season != "Autumn"]},
#            "Off": {"[True]": 0.95, "[False]": 1}}
#
# for key, value in tariffs["price"].items():
#     if any(value):
#         total_price = (tariffs["season type"][season] * key) * tariffs["Off"][str(tariffs["price"]["discount"])]
#         break
#
# left_over = abs(group_budget - total_price)
# if group_budget >= total_price:
#     print(f"Yes! You have {left_over:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {left_over:.2f} leva.")


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



# buget_group = int(input())
# weather_season = input()
# fisherman_numbers = int(input())
#
# fish_info = {"season rent": {
#     "Spring": 3000,
#     "Summer": 4200,
#     "Autumn": 4200,
#     "Winter": 2600},
#     "discount": {
#         "6 people": 0.10,
#         "7 - 11 people": 0.15,
#         "12 people": 0.25,
#         "5% off": 0.05}
# }
# even_discount = 0
# if fisherman_numbers <= 6:
#     total_discount = fish_info["season rent"][weather_season] - fish_info["season rent"][weather_season] * \
#                      fish_info["discount"]["6 people"]
# elif 7 <= fisherman_numbers <= 11:
#     total_discount = fish_info["season rent"][weather_season] - fish_info["season rent"][weather_season] * \
#                      fish_info["discount"]["7 - 11 people"]
# elif fisherman_numbers >= 12:
#     total_discount = fish_info["season rent"][weather_season] - fish_info["season rent"][weather_season] * \
#                      fish_info["discount"]["12 people"]
# if fisherman_numbers % 2 == 0 and "Autumn" not in weather_season:
#     even_discount = total_discount * fish_info["discount"]["5% off"]
# total_price = total_discount - even_discount
# if buget_group >= total_price:
#     money_left = buget_group - total_price
#     print(f"Yes! You have {money_left:.2f} leva left.")
# else:
#     money_left = total_price - buget_group
#     print(f"Not enough money! You need {money_left:.2f} leva.")
#
#

