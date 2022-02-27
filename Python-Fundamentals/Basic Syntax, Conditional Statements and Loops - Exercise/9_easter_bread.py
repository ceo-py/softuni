budget = float(input())
price_flour_kg = float(input())

eggs_price = price_flour_kg - (price_flour_kg * 0.25)
milk_price = (price_flour_kg + (price_flour_kg * 0.25)) / 4

budget_left = budget
bread_count = 0
eggs_counter = 0
total_budget = 0

while budget_left >= 0:
    budget_left = budget_left - (eggs_price + price_flour_kg + milk_price)

    if budget_left >= 0:
        eggs_counter += 3
        bread_count += 1
        total_budget = budget_left
        if bread_count % 3 == 0:
            eggs_counter = eggs_counter - (bread_count - 2)

print(
    f"You made {bread_count} loaves of Easter bread! Now you have {eggs_counter} eggs and {total_budget:.2f}BGN left.")