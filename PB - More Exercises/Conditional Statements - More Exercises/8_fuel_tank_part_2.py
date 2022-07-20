type_fuel = input()
quantity_fuel = float(input())
club_card = input()

price = 0
if type_fuel == "Diesel":
    price = 2.33
    if club_card == "Yes":
        price -= 0.12


elif type_fuel == "Gas":
    price = 0.93
    if club_card == "Yes":
        price -= 0.08


elif type_fuel == "Gasoline":
    price = 2.22
    if club_card == "Yes":
        price -= 0.18

total = price * quantity_fuel

if 20 <= quantity_fuel <= 25:
    total *= 0.92
elif quantity_fuel > 25:
    total *= 0.90

print(f"{total:.2f} lv.")








#
# type_fuel = input().lower()
# quantity_fuel = float(input())
# card = input().lower()
#
# fuel_info = {"diesel": {"diesel": 2.33, "yes": 0.12, "no": 0},
#             "gas": {"gas": 0.93, "yes": 0.08, "no": 0},
#             "gasoline": {"gasoline": 2.22, "yes": 0.18, "no": 0}}
# off_over_twenty_five_liters = 0.10
# off_between_twenty_and_twenty_five = 0.08
#
# if quantity_fuel <= 19:
#     total = (fuel_info[type_fuel][type_fuel] - fuel_info[type_fuel][card]) * quantity_fuel
# elif quantity_fuel <= 25:
#     total = (fuel_info[type_fuel][type_fuel] - fuel_info[type_fuel][card]) * quantity_fuel
#     total += - (total * off_between_twenty_and_twenty_five)
# elif quantity_fuel > 25:
#     total = (fuel_info[type_fuel][type_fuel] - fuel_info[type_fuel][card]) * quantity_fuel
#     total += - (total * off_over_twenty_five_liters)
#
# print(f"{total:.2f} lv.")
