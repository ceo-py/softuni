fuel_type = input().lower()
current_fuel_quantity = float(input())

if fuel_type in "diesel gasoline gas" and current_fuel_quantity >= 25:
    print(f"You have enough {fuel_type}.")
elif fuel_type in "diesel gasoline gas" and current_fuel_quantity < 25:
    print(f"Fill your tank with {fuel_type}!")
else:
    print("Invalid fuel!")



#
# fuel_type = input()
# current_fuel_quantity = float(input())
# diesel_fuel = "diesel"
# gasoline_fuel = "gasoline"
# gas_fuel = "gas"
# if fuel_type == "Diesel":
#     if current_fuel_quantity >= 25:
#         print(f"You have enough {diesel_fuel}.")
#     else:
#         print(f"Fill your tank with {diesel_fuel}!")
# elif fuel_type == "Gasoline":
#     if current_fuel_quantity >= 25:
#         print(f"You have enough {gasoline_fuel}.")
#     else:
#         print(f"Fill your tank with {gasoline_fuel}!")
# elif fuel_type == "Gas":
#     if current_fuel_quantity >= 25:
#         print(f"You have enough {gas_fuel}.")
#     else:
#         print(f"Fill your tank with {gas_fuel}!")
# else:
#     print("Invalid fuel!")




# fuel_type = input()
# fuel_capacity = int(input())
# fuel_type = fuel_type.lower()
#
# if fuel_type == "diesel" and fuel_capacity < 25:
#     print(f"Fill your tank with {fuel_type}!")
# elif fuel_type == "diesel" and fuel_capacity >= 25:
#     print(f"You have enough {fuel_type}.")
# elif fuel_type == "gasoline" and fuel_capacity < 25:
#     print(f"Fill your tank with {fuel_type}!")
# elif fuel_type == "gasoline" and fuel_capacity >= 25:
#     print(f"You have enough {fuel_type}.")
# elif fuel_type == "gas" and fuel_capacity < 25:
#     print(f"Fill your tank with {fuel_type}!")
# elif fuel_type == "gas" and fuel_capacity >= 25:
#     print(f"You have enough {fuel_type}.")
# else:
#     print("Invalid fuel!")





# fuel_type = input()
# fuel_capacity = int(input())
# fuel_type = fuel_type.lower()
#
# fuel_info = {
#     "diesel": "diesel",
#     "gasoline": "gasoline",
#     "gas": "gas"
# }
#
# if fuel_type in fuel_info and fuel_capacity < 25:
#     print(f"Fill your tank with {fuel_type}!")
# elif fuel_type in fuel_info and fuel_capacity >= 25:
#     print(f"You have enough {fuel_type}.")
# else:
#     print("Invalid fuel!")