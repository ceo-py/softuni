strawberries_price_lv = float(input())
quantity_bananas_in_kg = float(input())
quantity_oranges_in_kg = float(input())
quantity_raspberries_in_kg = float(input())
quantity_strawberries_in_kg = float(input())

raspberries_price = strawberries_price_lv / 2
oranges_price = raspberries_price - (raspberries_price * 0.40)
bananas_price = raspberries_price - (raspberries_price * 0.80)
raspberries_total = raspberries_price * quantity_raspberries_in_kg
oranges_total = oranges_price * quantity_oranges_in_kg
bananas_total = bananas_price * quantity_bananas_in_kg
strawberries_total = quantity_strawberries_in_kg * strawberries_price_lv
total = raspberries_total + oranges_total + bananas_total + strawberries_total

print(f"{total:.2f}")
