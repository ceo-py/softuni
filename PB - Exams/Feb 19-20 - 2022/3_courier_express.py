packages_kg = float(input())
service_type = input()
distance_km = int(input())

price = 0
additional_for_the_serves = 0
if 1 > packages_kg:
    price = 3
elif 10 > packages_kg:
    price = 5
elif 40 > packages_kg:
    price = 10
elif 90 > packages_kg:
    price = 15
elif 150 > packages_kg:
    price = 20

if service_type == "express":
    if 1 > packages_kg:
        additional_for_the_serves = price * 0.80
    elif 10 > packages_kg:
        additional_for_the_serves = price * 0.40
    elif 40 > packages_kg:
        additional_for_the_serves = price * 0.05
    elif 90 > packages_kg:
        additional_for_the_serves = price * 0.02
    elif 150 > packages_kg:
        additional_for_the_serves = price * 0.01
    additional_for_the_serves = (packages_kg * (additional_for_the_serves / 100)) * distance_km


total = additional_for_the_serves + (distance_km * price) / 100

print(f"The delivery of your shipment with weight of {packages_kg:.3f} kg. would cost {total:.2f} lv.")