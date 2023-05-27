budget = float(input())
season = str(input())

destination = ""

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        type_of_trip = 'Camp'
        trip_expense = budget * 0.30
    elif season == 'winter':
        type_of_trip = 'Hotel'
        trip_expense = budget * 0.70
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        type_of_trip = 'Camp'
        trip_expense = budget * 0.40
    elif season == 'winter':
        type_of_trip = 'Hotel'
        trip_expense = budget * 0.80
elif budget > 1000:
    destination = 'Europe'
    type_of_trip = 'Hotel'
    trip_expense = budget * 0.90

if destination:
    print(f"Somewhere in {destination}")
    print(f"{type_of_trip} - {trip_expense:.2f}")


# budget = float(input())
# season = str(input())
# trip_expense = 0
# destination = 0
# type_of_trip = 0
# if budget <= 100:
#     destination = 'Bulgaria'
#     if season == 'summer':
#         type_of_trip = 'Camp'
#         trip_expense = budget * 0.30
#     elif season == 'winter':
#         type_of_trip = 'Hotel'
#         trip_expense = budget * 0.70
# elif 100 < budget <= 1000:
#     destination = 'Balkans'
#     if season == 'summer':
#         type_of_trip = 'Camp'
#         trip_expense = budget * 0.40
#     elif season == 'winter':
#         type_of_trip = 'Hotel'
#         trip_expense = budget * 0.80
# elif budget > 1000:
#     destination = 'Europe'
#     type_of_trip = 'Hotel'
#     trip_expense = budget * 0.90
#
# if destination:
#     print(f"Somewhere in {destination}")
#     print(f"{type_of_trip} - {trip_expense:.2f}")



# budget = float(input())
# weather_season = input()
#
# budget_info = {100: {
#     1: "Bulgaria",
#     "summer": 0.30,
#     "winter": 0.70, },
#     1000: {
#         1: "Balkans",
#         "summer": 0.40,
#         "winter": 0.80, },
#     1001: {
#         1: "Europe",
#         "summer": 0.90,
#         "winter": 0.90, },
#     1: {
#         "summer": "Camp",
#         "winter": "Hotel"
#     }
#
# }
#
# if budget <= 100:
#     money_left = budget * budget_info[100][weather_season]
#     print(f"Somewhere in {budget_info[100][1]}\n{budget_info[1][weather_season]} - {money_left:.2f}")
# elif budget <= 1000:
#     money_left = budget * budget_info[1000][weather_season]
#     print(f"Somewhere in {budget_info[1000][1]}\n{budget_info[1][weather_season]} - {money_left:.2f}")
# elif budget > 1000:
#     money_left = budget * budget_info[1001][weather_season]
#     print(f"Somewhere in Europe\nHotel - {money_left:.2f}")
