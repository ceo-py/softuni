buget_group = int(input())
weather_season = input()
fisherman_numbers = int(input())

fish_info = {"season rent": {
    "Spring": 3000,
    "Summer": 4200,
    "Autumn": 4200,
    "Winter": 2600},
    "discount": {
        "6 people": 0.10,
        "7 - 11 people": 0.15,
        "12 people": 0.25,
        "5% off": 0.05}
}
even_discount = 0
if fisherman_numbers <= 6:
    total_discount = fish_info["season rent"][weather_season] - fish_info["season rent"][weather_season] * \
                     fish_info["discount"]["6 people"]
elif 7 <= fisherman_numbers <= 11:
    total_discount = fish_info["season rent"][weather_season] - fish_info["season rent"][weather_season] * \
                     fish_info["discount"]["7 - 11 people"]
elif fisherman_numbers >= 12:
    total_discount = fish_info["season rent"][weather_season] - fish_info["season rent"][weather_season] * \
                     fish_info["discount"]["12 people"]
if fisherman_numbers % 2 == 0 and "Autumn" not in weather_season:
    even_discount = total_discount * fish_info["discount"]["5% off"]
total_price = total_discount - even_discount
if buget_group >= total_price:
    money_left = buget_group - total_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_left = total_price - buget_group
    print(f"Not enough money! You need {money_left:.2f} leva.")
