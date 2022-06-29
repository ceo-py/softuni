vehicles = input().split(">>")

tax_info = {
    "family": {
        "tax": 50,
        "declines for every year": 5,
        "increase for km": 12,
        "traveled km": 3000
    },
    "heavyDuty": {
        "tax": 80,
        "declines for every year": 8,
        "increase for km": 14,
        "traveled km": 9000
    },
    "sports": {
        "tax": 100,
        "declines for every year": 9,
        "increase for km": 18,
        "traveled km": 2000
    }
}
total_tax_collected = 0
for car in vehicles:
    current_car_taxes = 0
    if any([True for car_type in list(tax_info.keys()) if car_type in car]):
        type_car, car_years, car_km = [int(x) if x.isdigit() else x for x in car.split()]
        current_car_taxes = tax_info[type_car]["tax"] + (
                int(car_km / tax_info[type_car]['traveled km']) * tax_info[type_car]['increase for km']) \
                            - (tax_info[type_car]["declines for every year"] * car_years)
        total_tax_collected += current_car_taxes
        print(f"A {type_car} car will pay {current_car_taxes:.2f} euros in taxes.")
    else:
        print(f"Invalid car type")

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")
