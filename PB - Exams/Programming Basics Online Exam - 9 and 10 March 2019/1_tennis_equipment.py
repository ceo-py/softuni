import math

price_tennis_racket = float(input())
total_tennis_racket = int(input())
number_tennis_sneakers = int(input())

rackets_total_price = price_tennis_racket * total_tennis_racket
one_sneakers_price = price_tennis_racket / 6
all_sneakers_price = one_sneakers_price * number_tennis_sneakers
total_price_equipment = rackets_total_price + all_sneakers_price + (rackets_total_price + all_sneakers_price) * 0.2

djokovic_price = total_price_equipment / 8
sponsors_price = total_price_equipment * (7 / 8)

print(f"Price to be paid by Djokovic {math.floor(djokovic_price)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_price)}")
