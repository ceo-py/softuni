budget = float(input())
video_cards = int(input())
procesors = int(input())
ram_memory = int(input())

video_cards_off = 0.15
video_cards_price_per_unit = 250
procesors_off = 0.35
ram_memory_off = 0.10
video_cards_total = video_cards * video_cards_price_per_unit
procesors_price = (video_cards_total * procesors_off) * procesors
ram_memory_price = (video_cards_total * ram_memory_off) * ram_memory
total_order_price = video_cards_total + procesors_price + ram_memory_price

if budget >= total_order_price:
    if video_cards > procesors:
        total_order_price += - total_order_price * video_cards_off
        total_order_price = budget - total_order_price
        print(f"You have {total_order_price:.2f} leva left!")
    else:
        total_order_price = budget - total_order_price
        print(f"You have {total_order_price:.2f} leva left!")
else:
    if video_cards > procesors:
        total_order_price += - total_order_price * video_cards_off
        total_order_price = total_order_price - budget
        print(f"Not enough money! You need {total_order_price:.2f} leva more!")
    else:
        total_order_price = total_order_price - budget
        print(f"Not enough money! You need {total_order_price:.2f} leva more!")
