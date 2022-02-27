import math

guests_number = int(input())
budget = int(input())

easter_cake = math.ceil(guests_number / 3)
eggs = guests_number * 2
easter_cake_price = easter_cake * 4
eggs_price = eggs * 0.45
total = eggs_price + easter_cake_price
money_left = abs(budget - total)

if budget >= total:
    print(f"Lyubo bought {easter_cake} Easter bread and {eggs} eggs.\nHe has {money_left:.2f} lv. left.")

else:
    print(f"Lyubo doesn't have enough money.\nHe needs {money_left:.2f} lv. more.")
