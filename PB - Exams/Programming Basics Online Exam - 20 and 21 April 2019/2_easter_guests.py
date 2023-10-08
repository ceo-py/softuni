from math import ceil

numbers_guests = int(input())
budget = int(input())

easter_bread_price = 4
egg_price = 0.45

easter_bread_needed = 3
egg_needed = 2

easter_bread_bought = ceil(numbers_guests / easter_bread_needed)
eggs_bread_bought = numbers_guests * egg_needed

total_sum = budget - ((easter_bread_bought * easter_bread_price) + (eggs_bread_bought * egg_price))

if total_sum >= 0:
    print(f'Lyubo bought {easter_bread_bought} Easter bread and {eggs_bread_bought} eggs.')
    print(f'He has {total_sum:.2f} lv. left.')
else:
    print("Lyubo doesn't have enough money.")
    print(f'He needs {abs(total_sum):.2f} lv. more.')




# import math
#
# guests_number = int(input())
# budget = int(input())
#
# easter_cake = math.ceil(guests_number / 3)
# eggs = guests_number * 2
# easter_cake_price = easter_cake * 4
# eggs_price = eggs * 0.45
# total = eggs_price + easter_cake_price
# money_left = abs(budget - total)
#
# if budget >= total:
#     print(f"Lyubo bought {easter_cake} Easter bread and {eggs} eggs.\nHe has {money_left:.2f} lv. left.")
#
# else:
#     print(f"Lyubo doesn't have enough money.\nHe needs {money_left:.2f} lv. more.")
