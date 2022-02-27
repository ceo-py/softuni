chrysanthemums_buy = int(input())
roses_buy = int(input())
tulips_buy = int(input())
season = input()
is_it_holiday = input()

flower_shop_info = {
    "Spring": {
        "chrysanthemums": 2.00,
        "tulips": 2.50,
        "roses": 4.10},
    "Summer": {
        "chrysanthemums": 2.00,
        "tulips": 2.50,
        "roses": 4.10},
    "Autumn": {
        "chrysanthemums": 3.75,
        "tulips": 4.15,
        "roses": 4.50},
    "Winter": {
        "chrysanthemums": 3.75,
        "tulips": 4.15,
        "roses": 4.50},
    "Off": {
        "7 > tulips spring": 0.05,
        "10 > roses winter": 0.10,
        "20 > all seasons": 0.20}
}
holiday_prices = 0.15
total_flowers_buy = chrysanthemums_buy + roses_buy + tulips_buy
creating_bucket = 2
chrysanthemums_prices = chrysanthemums_buy * flower_shop_info[season]["chrysanthemums"]
roses_prices = roses_buy * flower_shop_info[season]["roses"]
tulips_prices = tulips_buy * flower_shop_info[season]["tulips"]
total = (chrysanthemums_prices + roses_prices + tulips_prices)

if is_it_holiday == "Y":
    holiday_added = (chrysanthemums_prices + roses_prices + tulips_prices) * holiday_prices
    total +=  + holiday_added
    if tulips_buy > 7 and season == "Spring":
        total += - (total * flower_shop_info["Off"]["7 > tulips spring"])
    if roses_buy >= 10 and season == "Winter":
        total += - (total * flower_shop_info["Off"]["10 > roses winter"])
    if total_flowers_buy > 20:
        total += - (total * flower_shop_info["Off"]["20 > all seasons"])
else:
    if tulips_buy > 7 and season == "Spring":
        total += - (total * flower_shop_info["Off"]["7 > tulips spring"])
    if roses_buy >= 10 and season == "Winter":
        total += - (total * flower_shop_info["Off"]["10 > roses winter"])
    if total_flowers_buy > 20:
        total += - (total * flower_shop_info["Off"]["20 > all seasons"])

total += + creating_bucket
print(f"{total:.2f}")