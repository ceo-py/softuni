shop_items = {}

stock_fill = input()

while stock_fill != "shopping time":
    stock_fill = stock_fill.split()
    if stock_fill[1] not in shop_items:
        shop_items[stock_fill[1]] = 0
    shop_items[stock_fill[1]] += int(stock_fill[-1])
    stock_fill = input()

buy_products = input()

while buy_products != "exam time":
    buy_products = buy_products.split()
    if buy_products[1] not in shop_items:
        print(f"{buy_products[1]} doesn't exist")
    elif buy_products[1] in shop_items and shop_items[buy_products[1]] <= 0:
        print(f"{buy_products[1]} out of stock")
    else:
        shop_items[buy_products[1]] -= int(buy_products[2])
    buy_products = input()

for key, value in shop_items.items():
    if value > 0:
        print(f"{key} -> {value}")
