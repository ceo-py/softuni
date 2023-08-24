drink = input()
sugar = input()
drink_numbers = int(input())

drink_price = 0

if drink == 'Espresso':

    if sugar == 'Without':
        drink_price = 0.90

    elif sugar == 'Normal':
        drink_price = 1

    elif sugar == 'Extra':
        drink_price = 1.20


elif drink == 'Cappuccino':

    if sugar == 'Without':
        drink_price = 1

    elif sugar == 'Normal':
        drink_price = 1.20

    elif sugar == 'Extra':
        drink_price = 1.60

elif drink == 'Tea':

    if sugar == 'Without':
        drink_price = 0.50

    elif sugar == 'Normal':
        drink_price = 0.60

    elif sugar == 'Extra':
        drink_price = 0.70

if sugar == 'Without':
    drink_price *= 0.65

if drink == 'Espresso' and drink_numbers >= 5:
    drink_price *= 0.75

total_price = drink_price * drink_numbers

if total_price > 15:
    total_price *= 0.80

print(f'You bought {drink_numbers} cups of {drink} for {total_price:.2f} lv.')








# type_of_drink = input()
# sugar_amount = input()
# count_drinks = int(input())
# price_per_drink = 0
#
# if type_of_drink == "Espresso":
#     price_per_drink = 0.9
#     if sugar_amount == "Normal":
#         price_per_drink = 1
#     elif sugar_amount == "Extra":
#         price_per_drink = 1.2
#
# if type_of_drink == "Cappuccino":
#     price_per_drink = 1
#     if sugar_amount == "Normal":
#         price_per_drink = 1.2
#     elif sugar_amount == "Extra":
#         price_per_drink = 1.6
#
# if type_of_drink == "Tea":
#     price_per_drink = 0.5
#     if sugar_amount == "Normal":
#         price_per_drink = 0.6
#     elif sugar_amount == "Extra":
#         price_per_drink = 0.7
#
# bill = price_per_drink * count_drinks
#
# if sugar_amount == "Without":
#     bill *= 0.65
#
# if type_of_drink == "Espresso" and count_drinks >= 5:
#     bill *= 0.75
#
# if bill > 15:
#     bill *= 0.8
#
# print(f'You bought {count_drinks} cups of {type_of_drink} for {bill:.2f} lv.')




# type_drink = input()
# sugar = input()
# number_of_drinks = int(input())
# drink = 0
# if type_drink == "Espresso" and sugar == "Without":
#     drink = 0.9 * number_of_drinks
# elif type_drink == "Espresso" and sugar == "Normal":
#     drink = 1 * number_of_drinks
# elif type_drink == "Espresso" and sugar == "Extra":
#     drink = 1.2 * number_of_drinks
#
# if type_drink == "Cappuccino" and sugar == "Without":
#     drink = 1 * number_of_drinks
# elif type_drink == "Cappuccino" and sugar == "Normal":
#     drink = 1.2 * number_of_drinks
# elif type_drink == "Cappuccino" and sugar == "Extra":
#     drink = 1.6 * number_of_drinks
#
# if type_drink == "Tea" and sugar == "Without":
#     drink = 0.5 * number_of_drinks
# elif type_drink == "Tea" and sugar == "Normal":
#     drink = 0.6 * number_of_drinks
# elif type_drink == "Tea" and sugar == "Extra":
#     drink = 0.7 * number_of_drinks
#
# if sugar == "Without":
#     drink *= 0.65
#
# if type_drink == "Espresso" and number_of_drinks >= 5:
#     drink *= 0.75
#
# if drink > 15:
#     drink *= 0.80
#
#
# print(f"You bought {number_of_drinks} cups of {type_drink} for {drink:.2f} lv.")
#



# drink_type = input()
# sugar_type = input()
# number_of_drinks = int(input())
#
# drink_info = {
#     "Espresso": {
#         "Without": 0.90,
#         "Normal": 1,
#         "Extra": 1.20},
#     "Cappuccino": {
#         "Without": 1,
#         "Normal": 1.20,
#         "Extra": 1.60},
#     "Tea": {
#         "Without": 0.50,
#         "Normal": 0.60,
#         "Extra": 0.70},
#
# }
#
# total = drink_info[drink_type][sugar_type] * number_of_drinks
#
# if sugar_type == "Without":
#     total = total - (total * 0.35)
#
# if drink_type == "Espresso" and number_of_drinks >= 5:
#     total = total - (total * 0.25)
#
# if total > 15:
#     total = total - (total * 0.20)
#
# print(f"You bought {number_of_drinks} cups of {drink_type} for {total:.2f} lv.")




# type_drink = input()
# sugar = input()
# number_of_drinks = int(input())
# price = 1
#
# if sugar == "Without":
#     if type_drink.startswith("E"):
#         price = 0.9
#     elif type_drink.startswith("C"):
#         price = 1
#     elif type_drink.startswith("T"):
#         price = 0.5
#
# elif sugar == "Normal":
#     if type_drink.startswith("E"):
#         price = 1
#     elif type_drink.startswith("C"):
#         price = 1.2
#     elif type_drink.startswith("T"):
#         price = 0.6
#
# elif sugar == "Extra":
#     if type_drink.startswith("E"):
#         price = 1.2
#     elif type_drink.startswith("C"):
#         price = 1.6
#     elif type_drink.startswith("T"):
#         price = 0.7
#
# total_price = price * number_of_drinks
#
# if sugar == "Without":
#     total_price *= 0.65
#
# if type_drink == "Espresso" and number_of_drinks >= 5:
#     total_price *= 0.75
#
# if total_price > 15:
#     total_price *= 0.80
#
# print(f"You bought {number_of_drinks} cups of {type_drink} for {total_price:.2f} lv.")


