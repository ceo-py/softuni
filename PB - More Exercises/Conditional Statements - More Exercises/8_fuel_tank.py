fuel_type = input()
fuel_capacity = int(input())
fuel_type = fuel_type.lower()

fuel_info = {
    "diesel": "diesel",
    "gasoline": "gasoline",
    "gas": "gas"
}

if fuel_type in fuel_info and fuel_capacity < 25:
    print(f"Fill your tank with {fuel_type}!")
elif fuel_type in fuel_info and fuel_capacity >= 25:
    print(f"You have enough {fuel_type}.")
else:
    print("Invalid fuel!")