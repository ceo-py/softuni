drink_type = input()
sugar_type = input()
number_of_drinks = int(input())

drink_info = {
    "Espresso": {
        "Without": 0.90,
        "Normal": 1,
        "Extra": 1.20},
    "Cappuccino": {
        "Without": 1,
        "Normal": 1.20,
        "Extra": 1.60},
    "Tea": {
        "Without": 0.50,
        "Normal": 0.60,
        "Extra": 0.70},

}

total = drink_info[drink_type][sugar_type] * number_of_drinks

if sugar_type == "Without":
    total = total - (total * 0.35)

if drink_type == "Espresso" and number_of_drinks >= 5:
    total = total - (total * 0.25)

if total > 15:
    total = total - (total * 0.20)

print(f"You bought {number_of_drinks} cups of {drink_type} for {total:.2f} lv.")