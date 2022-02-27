frud = input()
set_available = input()
order_set = int(input())


watermalone_small = 56
watermalone_big = 28.70
mango_small = 36.66
mango_big = 19.60
pinapple_small = 42.10
pinapple_big = 24.80
malina_small = 20
malina_big = 15.20
fourhundred_off = 0.15
onethousand = 0.50

if "Watermelon" in frud:
    if "big" in set_available:
        total = 5 * watermalone_big
        set_price = order_set * total
        if 400 <= set_price <= 1000:
            set_price = set_price - set_price * fourhundred_off
        elif set_price > 1000:
            set_price = set_price - set_price * onethousand
    elif "small" in set_available:
        total = 2 * watermalone_small
        set_price = order_set * total
        if 400 <= set_price <= 1000:
            set_price = set_price - set_price * fourhundred_off
        elif set_price > 1000:
            set_price = set_price - set_price * onethousand
elif "Mango" in frud:
    if "big" in set_available:
        total = 5 * mango_big
        set_price = order_set * total
        if 400 <= set_price <= 1000:
            set_price = set_price - set_price * fourhundred_off
        elif set_price > 1000:
            set_price = set_price - set_price * onethousand
    elif "small" in set_available:
        total = 2 * mango_small
        set_price = order_set * total
        if 400 <= set_price <= 1000:
            set_price = set_price - set_price * fourhundred_off
        elif set_price > 1000:
            set_price = set_price - set_price * onethousand
elif "Pineapple" in frud:
    if "big" in set_available:
        total = 5 * pinapple_big
        set_price = order_set * total
        if 400 <= set_price <= 1000:
            set_price = set_price - set_price * fourhundred_off
        elif set_price > 1000:
            set_price = set_price - set_price * onethousand
    elif "small" in set_available:
        total = 2 * pinapple_small
        set_price = order_set * total
        if 400 <= set_price <= 1000:
            set_price = set_price - set_price * fourhundred_off
        elif set_price > 1000:
            set_price = set_price - set_price * onethousand
elif "Raspberry" in frud:
    if "big" in set_available:
        total = 5 * malina_big
        set_price = order_set * total
        if 400 <= set_price <= 1000:
            set_price = set_price - set_price * fourhundred_off
        elif set_price > 1000:
            set_price = set_price - set_price * onethousand
    elif "small" in set_available:
        total = 2 * malina_small
        set_price = order_set * total
        if 400 <= set_price <= 1000:
            set_price = set_price - set_price * fourhundred_off
        elif set_price > 1000:
            set_price = set_price - set_price * onethousand

print(f"{set_price:.2f} lv.")