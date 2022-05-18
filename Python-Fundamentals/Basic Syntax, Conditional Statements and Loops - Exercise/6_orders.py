number_orders = int(input())

total = 0

for _ in range(number_orders):
    price_per_capsule = float(input())
    days = int(input())
    count_capsule = int(input())
    single_order = price_per_capsule * days * count_capsule
    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= count_capsule <= 2000:
        total += single_order
        print(f"The price for the coffee is: ${single_order:.2f}")

print(f"Total: ${total:.2f}")
