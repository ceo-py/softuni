type_food = input()
days_of_the_week = input()
quantity = float(input())

prices = {"week": {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85},
    "weekend": {
        "banana": 2.70,
        "apple": 1.25,
        "orange": 0.90,
        "grapefruit": 1.60,
        "kiwi": 3.00,
        "pineapple": 5.60,
        "grapes": 4.20},
}

working_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
day_check = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
if days_of_the_week in day_check and type_food in prices["week"]:
    if days_of_the_week in working_days:
        total = prices["week"][type_food] * quantity
        print("{:.2f}".format(total))
    elif days_of_the_week in day_check:
        total = prices["weekend"][type_food] * quantity
        print("{:.2f}".format(total))
else:
    print("error")
