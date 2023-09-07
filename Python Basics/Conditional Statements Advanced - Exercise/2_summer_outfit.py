degrees = int(input())
time_of_the_day = input()

outfit = ''
shoes = ''

if 10 <= degrees <= 18:

    if time_of_the_day == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'

    elif time_of_the_day == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'

    elif time_of_the_day == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

elif degrees <= 24:

    if time_of_the_day == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'

    elif time_of_the_day == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'

    elif time_of_the_day == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

elif degrees >= 25:

    if time_of_the_day == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'

    elif time_of_the_day == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

    elif time_of_the_day == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")





# degrees = int(input())
# time_of_the_day = input()
#
# outfit = None
# shoes = None
#
# if 10 <= degrees <= 18:
#     if time_of_the_day == "Morning":
#         outfit = "Sweatshirt"
#         shoes = "Sneakers"
#     elif time_of_the_day == "Afternoon":
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif time_of_the_day == "Evening":
#         outfit = "Shirt"
#         shoes = "Moccasins"
#
# elif 18 < degrees <= 24:
#     if time_of_the_day == "Morning":
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif time_of_the_day == "Afternoon":
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     elif time_of_the_day == "Evening":
#         outfit = "T-Shirt"
#         shoes = "Moccasins"
#
# elif degrees >= 25:
#     if time_of_the_day == "Morning":
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     elif time_of_the_day == "Afternoon":
#         outfit = "Swim Suit"
#         shoes = "Barefoot"
#     elif time_of_the_day == "Evening":
#         outfit = "Shirt"
#         shoes = "Moccasins"
#
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")




# tempreture_celsius = int(input())
# weather_time = input()
#
# outfits_depending_on_time = {
#     "Outfit 10 - 18": ["Sweatshirt", "Shirt", "Shirt"],
#     "Shoes 10 - 18": ["Sneakers", "Moccasins", "Moccasins"],
#     "Outfit 18 - 24": ["Shirt", "T-Shirt", "Shirt"],
#     "Shoes 18 - 24": ["Moccasins", "Sandals", "Moccasins"],
#     "Outfit => 25": ["T-Shirt", "Swim Suit", "Shirt"],
#     "Shoes => 25": ["Sandals", "Barefoot", "Moccasins"],
#     "Morning": 0,"Afternoon": 1,"Evening":2}
#
# if 10 <= tempreture_celsius <= 18:
#     outfit = outfits_depending_on_time["Outfit 10 - 18"][outfits_depending_on_time[weather_time]]
#     shoes = outfits_depending_on_time["Shoes 10 - 18"][outfits_depending_on_time[weather_time]]
# elif tempreture_celsius <= 24:
#     outfit = outfits_depending_on_time["Outfit 18 - 24"][outfits_depending_on_time[weather_time]]
#     shoes = outfits_depending_on_time["Shoes 18 - 24"][outfits_depending_on_time[weather_time]]
# elif tempreture_celsius >= 24:
#     outfit = outfits_depending_on_time["Outfit => 25"][outfits_depending_on_time[weather_time]]
#     shoes = outfits_depending_on_time["Shoes => 25"][outfits_depending_on_time[weather_time]]
# print(f"It's {tempreture_celsius} degrees, get your {outfit} and {shoes}.")


# tempreture_celsius = int(input())
# weather_time = input()
#
# outfits_depending_on_time = {"Morning": {
#     "Outfit 10 - 18": "Sweatshirt",
#     "Shoes 10 - 18": "Sneakers",
#     "Outfit 18 - 24": "Shirt",
#     "Shoes 18 - 24": "Moccasins",
#     "Outfit => 25": "T-Shirt",
#     "Shoes => 25": "Sandals", },
#     "Afternoon": {
#         "Outfit 10 - 18": "Shirt",
#         "Shoes 10 - 18": "Moccasins",
#         "Outfit 18 - 24": "T-Shirt",
#         "Shoes 18 - 24": "Sandals",
#         "Outfit => 25": "Swim Suit",
#         "Shoes => 25": "Barefoot", },
#     "Evening": {
#         "Outfit 10 - 18": "Shirt",
#         "Shoes 10 - 18": "Moccasins",
#         "Outfit 18 - 24": "Shirt",
#         "Shoes 18 - 24": "Moccasins",
#         "Outfit => 25": "Shirt",
#         "Shoes => 25": "Moccasins", }
# }
#
# if 10 <= tempreture_celsius <= 18:
#     outfit = outfits_depending_on_time[weather_time]["Outfit 10 - 18"]
#     shoes = outfits_depending_on_time[weather_time]["Shoes 10 - 18"]
#     print(f"It's {tempreture_celsius} degrees, get your {outfit} and {shoes}.")
# elif 18 < tempreture_celsius <= 24:
#     outfit = outfits_depending_on_time[weather_time]["Outfit 18 - 24"]
#     shoes = outfits_depending_on_time[weather_time]["Shoes 18 - 24"]
#     print(f"It's {tempreture_celsius} degrees, get your {outfit} and {shoes}.")
# elif tempreture_celsius >= 24:
#     outfit = outfits_depending_on_time[weather_time]["Outfit => 25"]
#     shoes = outfits_depending_on_time[weather_time]["Shoes => 25"]
#     print(f"It's {tempreture_celsius} degrees, get your {outfit} and {shoes}.")
