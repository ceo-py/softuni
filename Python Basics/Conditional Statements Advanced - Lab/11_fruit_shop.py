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





# fruit = input()
# day_of_week = input()
# quantity = float(input())
#
# fruits = {
#     "banana": [2.50, 2.70],
#     "apple": [1.20, 1.25],
#     "grapefruit": [1.45, 1.60],
#     "kiwi": [2.70, 3.00],
#     "grapes": [3.85, 4.20],
#     "orange": [0.85, 0.90],
#     "pineapple": [5.50, 5.60],
#     'Sunday': 1,
#     'Saturday': 1,
# }
#
# week_days = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
#
# if day_of_week not in week_days or fruit not in fruits:
#     print('error')
# else:
#     price = fruits[fruit][fruits.get(day_of_week, 0)]
#     total_price = quantity * price
#     print(f'{total_price:.2f}')
