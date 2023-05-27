fruit = input()
day_of_week = input()
quantity = float(input())

banana_price = 2.50
apple_price = 1.20
orange_price = 0.85
grapefruit_price = 1.45
kiwi_price = 2.70
pineapple_price = 5.50
grapes_price = 3.85
price = 0

week_days = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
correct_fruits = "banana, apple, grapefruit, kiwi, grapes, orange, pineapple"

if day_of_week not in week_days or fruit not in correct_fruits:
    print('error')
else:
    if day_of_week == 'Sunday' or day_of_week == 'Saturday':
        banana_price = 2.70
        apple_price = 1.25
        orange_price = 0.90
        grapefruit_price = 1.60
        kiwi_price = 3.00
        pineapple_price = 5.60
        grapes_price = 4.20

    if fruit == 'banana':
        price = banana_price

    elif fruit == 'apple':
        price = apple_price

    elif fruit == 'grapefruit':
        price = grapefruit_price

    elif fruit == 'kiwi':
        price = kiwi_price

    elif fruit == 'grapes':
        price = grapes_price

    elif fruit == 'orange':
        price = orange_price

    elif fruit == 'pineapple':
        price = pineapple_price

    total_price = quantity * price
    print(f'{total_price:.2f}')







#
# fruit = input()
# day = input()
# count = float(input())
#
# price = 0
#
# if fruit == 'banana':
#     if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
#         price = 2.50
#
# elif fruit == 'apple':
#     if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
#         price = 1.20
#
# elif fruit == 'orange':
#     if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
#         price = 0.85
#
# elif fruit == 'grapefruit':
#     if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
#         price = 1.45
#
# elif fruit == 'kiwi':
#     if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
#         price = 2.70
#
# elif fruit == 'pineapple':
#     if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
#         price = 5.50
#
# elif fruit == 'grapes':
#     if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
#         price = 3.85
#
# if fruit == 'banana':
#     if day == 'Saturday' or day == 'Sunday':
#         price = 2.70
#
# elif fruit == 'apple':
#     if day == 'Saturday' or day == 'Sunday':
#         price = 1.25
#
# elif fruit == 'orange':
#     if day == 'Saturday' or day == 'Sunday':
#         price = 0.90
#
# elif fruit == 'grapefruit':
#     if day == 'Saturday' or day == 'Sunday':
#         price = 1.60
#
# elif fruit == 'kiwi':
#     if day == 'Saturday' or day == 'Sunday':
#         price = 3.00
#
# elif fruit == 'pineapple':
#     if day == 'Saturday' or day == 'Sunday':
#         price = 5.60
#
# elif fruit == 'grapes':
#     if day == 'Saturday' or day == 'Sunday':
#         price = 4.20
#
# if price:
#     total = price * count
#     print(f'{total:.2f}')
# else:
#     print('error')
#






# fruit = input()
# day_of_week = input()
# quantity = float(input())
#
# banana_price = 2.50
# apple_price = 1.20
# orange_price = 0.85
# grapefruit_price = 1.45
# kiwi_price = 2.70
# pineapple_price = 5.50
# grapes_price = 3.85
# price = 0
#
# week_days = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
# correct_fruits = "banana, apple, grapefruit, kiwi, grapes, orange, pineapple"
#
# if day_of_week not in week_days or fruit not in correct_fruits:
#     print('error')
# else:
#     if day_of_week == 'Sunday' or day_of_week == 'Saturday':
#         banana_price = 2.70
#         apple_price = 1.25
#         orange_price = 0.90
#         grapefruit_price = 1.60
#         kiwi_price = 3.00
#         pineapple_price = 5.60
#         grapes_price = 4.20
#
#     if fruit == 'banana':
#         price = banana_price
#
#     elif fruit == 'apple':
#         price = apple_price
#
#     elif fruit == 'grapefruit':
#         price = grapefruit_price
#
#     elif fruit == 'kiwi':
#         price = kiwi_price
#
#     elif fruit == 'grapes':
#         price = grapes_price
#
#     elif fruit == 'orange':
#         price = orange_price
#
#     elif fruit == 'pineapple':
#         price = pineapple_price
#
#     total_price = quantity * price
#     print(f'{total_price:.2f}')
#





#
#
# product = input()
# day = input()
# quality = float(input())
# price = 0
# if day in ['Saturday', 'Sunday']:
#     if product == 'banana':
#         price = quality * 2.70
#     elif product == 'apple':
#         price = quality * 1.25
#     elif product == 'orange':
#         price = quality * 0.90
#     elif product == 'grapefruit':
#         price = quality * 1.60
#     elif product == 'kiwi':
#         price = quality * 3.00
#     elif product == 'pineapple':
#         price = quality * 5.60
#     elif product == 'grapes':
#         price = quality * 4.20
#     if price:
#         print(f'{price:.2f}')
#     else:
#         print('error')
# elif day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
#     if product == 'banana':
#         price = quality * 2.50
#     elif product == 'apple':
#         price = quality * 1.20
#     elif product == 'orange':
#         price = quality * 0.85
#     elif product == 'grapefruit':
#         price = quality * 1.45
#     elif product == 'kiwi':
#         price = quality * 2.70
#     elif product == 'pineapple':
#         price = quality * 5.50
#     elif product == 'grapes':
#         price = quality * 3.85
#     if price:
#         print(f'{price:.2f}')
#     else:
#         print('error')
# else:
#     print('error')
#
#






# type_food = input()
# days_of_the_week = input()
# quantity = float(input())
#
# prices = {
#     "banana": [2.50, 2.70],
#     "apple": [1.20, 1.25],
#     "orange": [0.85, 0.90],
#     "grapefruit": [1.45, 1.60],
#     "kiwi": [2.70, 3.00],
#     "pineapple": [5.50, 5.60],
#     "grapes": [3.85, 4.20],
#     "weekend": 1,
#     "week": 0}
#
# working_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# day_check = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# if days_of_the_week in day_check and type_food in prices:
#     if days_of_the_week in working_days:
#         total = prices[type_food][prices["week"]] * quantity
#     elif days_of_the_week in day_check:
#         total = prices[type_food][prices["weekend"]] * quantity
#     print(f"{(round(total, 2)):.2f}")
# else:
#     print("error")
#
#









# fruit = input()
# day_of_week = input()
# quantity = float(input())
#
# data_for = {
#     "banana": (2.50, 2.70),
#     "apple": (1.20, 1.25),
#     "grapefruit": (1.45, 1.60),
#     "kiwi": (2.70, 3.00),
#     "grapes": (3.85, 4.20),
#     "orange": (0.85, 0.90),
#     "pineapple": (5.50, 5.60),
#     "Sunday": 1,
#     "Saturday": 1,
#     "week days": ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# }
#
#
# if day_of_week not in data_for["week days"] or fruit not in data_for:
#     print('error')
# else:
#     total_price = quantity * data_for[fruit][data_for.get(day_of_week, 0)]
#     print(f'{total_price:.2f}')



# type_food = input()
# days_of_the_week = input()
# quantity = float(input())
#
# prices = {"week": {
#     "banana": 2.50,
#     "apple": 1.20,
#     "orange": 0.85,
#     "grapefruit": 1.45,
#     "kiwi": 2.70,
#     "pineapple": 5.50,
#     "grapes": 3.85},
#     "weekend": {
#         "banana": 2.70,
#         "apple": 1.25,
#         "orange": 0.90,
#         "grapefruit": 1.60,
#         "kiwi": 3.00,
#         "pineapple": 5.60,
#         "grapes": 4.20},
# }
#
# working_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# day_check = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# if days_of_the_week in day_check and type_food in prices["week"]:
#     if days_of_the_week in working_days:
#         total = prices["week"][type_food] * quantity
#         print("{:.2f}".format(round(total, 2)))
#     elif days_of_the_week in day_check:
#         total = prices["weekend"][type_food] * quantity
#         print("{:.2f}".format(round(total, 2)))
# else:
#     print("error")
#


# fruit = input()
# day_of_week = input()
# quantity = float(input())
#
# banana_price = 2.50
# apple_price = 1.20
# orange_price = 0.85
# grapefruit_price = 1.45
# kiwi_price = 2.70
# pineapple_price = 5.50
# grapes_price = 3.85
# price = 0
#
#
# if day_of_week != "Monday" and day_of_week != "Tuesday" and day_of_week != "Wednesday" and \
#         day_of_week != "Thursday" and day_of_week != "Friday" and day_of_week != "Saturday" \
#         and day_of_week != "Sunday" or fruit != 'banana' and fruit != 'apple' and fruit != 'grapefruit' \
#         and fruit != 'kiwi' and fruit != 'grapes' and fruit != 'orange' and fruit != 'pineapple':
#     print('error')
# else:
#     if day_of_week == 'Sunday' or day_of_week == 'Saturday':
#         banana_price = 2.70
#         apple_price = 1.25
#         orange_price = 0.90
#         grapefruit_price = 1.60
#         kiwi_price = 3.00
#         pineapple_price = 5.60
#         grapes_price = 4.20
#
#     if fruit == 'banana':
#         price = banana_price
#
#     elif fruit == 'apple':
#         price = apple_price
#
#     elif fruit == 'grapefruit':
#         price = grapefruit_price
#
#     elif fruit == 'kiwi':
#         price = kiwi_price
#
#     elif fruit == 'grapes':
#         price = grapes_price
#
#     elif fruit == 'orange':
#         price = orange_price
#
#     elif fruit == 'pineapple':
#         price = pineapple_price
#     total_price = quantity * price
#     print(f'{total_price:.2f}')
#
#