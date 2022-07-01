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


if day_of_week != "Monday" and day_of_week != "Tuesday" and day_of_week != "Wednesday" and \
        day_of_week != "Thursday" and day_of_week != "Friday" and day_of_week != "Saturday" \
        and day_of_week != "Sunday" or fruit != 'banana' and fruit != 'apple' and fruit != 'grapefruit' \
        and fruit != 'kiwi' and fruit != 'grapes' and fruit != 'orange' and fruit != 'pineapple':
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
#
#
#
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
#
# day_check = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# if days_of_the_week in day_check and type_food in prices:
#     if days_of_the_week in day_check[:5]:
#         total = prices[type_food][prices["week"]] * quantity
#     else:
#         total = prices[type_food][prices["weekend"]] * quantity
#     print(f"{total:.2f}")
# else:
#     print("error")
