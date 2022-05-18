product = input()
city = input()
quantity = float(input())

info = {
    "coffee": [0.50, 0.40, 0.45],
    "water": [0.80, 0.70, 0.70],
    "beer": [1.20, 1.15, 1.10],
    "sweets": [1.45, 1.30, 1.35],
    "peanuts": [1.60, 1.50, 1.55],
    "Sofia": 0, "Plovdiv": 1, "Varna": 2,
}

check_to_pay = info[product][info[city]] * quantity
print(round(check_to_pay, 2))

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
