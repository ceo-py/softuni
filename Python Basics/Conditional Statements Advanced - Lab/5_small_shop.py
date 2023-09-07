product = input()
city = input()
quantity = float(input())

product_price = 0

if city == 'Sofia':

    if product == 'coffee':
        product_price = 0.50

    elif product == 'water':
        product_price = 0.80

    elif product == 'beer':
        product_price = 1.20

    elif product == 'sweets':
        product_price = 1.45

    elif product == 'peanuts':
        product_price = 1.60


elif city == 'Plovdiv':

    if product == 'coffee':
        product_price = 0.40

    elif product == 'water':
        product_price = 0.70

    elif product == 'beer':
        product_price = 1.15

    elif product == 'sweets':
        product_price = 1.30

    elif product == 'peanuts':
        product_price = 1.50

elif city == 'Varna':

    if product == 'coffee':
        product_price = 0.45

    elif product == 'water':
        product_price = 0.70

    elif product == 'beer':
        product_price = 1.10

    elif product == 'sweets':
        product_price = 1.35

    elif product == 'peanuts':
        product_price = 1.55

total_sum = product_price * quantity

print(total_sum)


# product = input()
# city = input()
# quantity = float(input())
#
# info = {
#     "coffee": [0.50, 0.40, 0.45],
#     "water": [0.80, 0.70, 0.70],
#     "beer": [1.20, 1.15, 1.10],
#     "sweets": [1.45, 1.30, 1.35],
#     "peanuts": [1.60, 1.50, 1.55],
#     "Sofia": 0, "Plovdiv": 1, "Varna": 2,
# }
#
# check_to_pay = info[product][info[city]] * quantity
# print(round(check_to_pay, 2))






# product = input()
# city = input()
# quantity = float(input())
#
# town = {"Sofia": {
#     "coffee": 0.50,
#     "water": 0.80,
#     "beer": 1.20,
#     "sweets": 1.45,
#     "peanuts": 1.60},
#
#     "Plovdiv": {
#         "coffee": 0.40,
#         "water": 0.70,
#         "beer": 1.15,
#         "sweets": 1.30,
#         "peanuts": 1.50},
#
#     "Varna": {
#         "coffee": 0.45,
#         "water": 0.70,
#         "beer": 1.10,
#         "sweets": 1.35,
#         "peanuts": 1.55
#     }
# }
#
# check_to_pay = town[city][product] * quantity
# print(round(check_to_pay, 2))
