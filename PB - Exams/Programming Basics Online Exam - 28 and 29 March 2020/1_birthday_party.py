rent = int(input())
cake_price = rent * 0.20
drink_price = cake_price - cake_price * 0.45
animator = rent / 3
total_price = rent + cake_price + drink_price + animator
print(total_price)
