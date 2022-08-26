fruit = input()
size_set = input()
number_order_sets = int(input())

price = 0
number_in_set = 0

if "small" == size_set:
    number_in_set = 2
    if "Watermelon" == fruit:
        price = 56
    elif "Mango" == fruit:
        price = 36.66
    elif "Pineapple" == fruit:
        price = 42.10
    elif "Raspberry" == fruit:
        price = 20

elif "big" == size_set:
    number_in_set = 5
    if "Watermelon" == fruit:
        price = 28.70
    elif "Mango" == fruit:
        price = 19.60
    elif "Pineapple" == fruit:
        price = 24.80
    elif "Raspberry" == fruit:
        price = 15.20

total_price = number_in_set * price * number_order_sets

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50

print(f"{total_price:.2f} lv.")