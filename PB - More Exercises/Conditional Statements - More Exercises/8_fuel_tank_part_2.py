type_fuel = input().lower()
quantity_fuel = float(input())
card = input().lower()

fuel_info = {"diesel": {"diesel": 2.33, "yes": 0.12, "no": 0},
            "gas": {"gas": 0.93, "yes": 0.08, "no": 0},
            "gasoline": {"gasoline": 2.22, "yes": 0.18, "no": 0}}
off_over_twenty_five_liters = 0.10
off_between_twenty_and_twenty_five = 0.08

if quantity_fuel <= 19:
    total = (fuel_info[type_fuel][type_fuel] - fuel_info[type_fuel][card]) * quantity_fuel
elif quantity_fuel <= 25:
    total = (fuel_info[type_fuel][type_fuel] - fuel_info[type_fuel][card]) * quantity_fuel
    total += - (total * off_between_twenty_and_twenty_five)
elif quantity_fuel > 25:
    total = (fuel_info[type_fuel][type_fuel] - fuel_info[type_fuel][card]) * quantity_fuel
    total += - (total * off_over_twenty_five_liters)

print(f"{total:.2f} lv.")
