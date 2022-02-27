vegetables_price_per_kg = float(input())
fruits_price_per_kg = float(input())
total_vegetables = float(input())
total_fruits = float(input())

total_price = ((vegetables_price_per_kg * total_vegetables) + (fruits_price_per_kg * total_fruits)) / 1.94

print(f"{total_price:.2f}")