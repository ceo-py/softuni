budget = float(input())
category = input()
people_count = float(input())

trip_info = {
    1: 0.75,
    5: 0.60,
    10: 0.50,
    25: 0.40,
    50: 0.25,
    "VIP": 499.99,
    "Normal": 249.99
}

if 1 <= people_count <= 4:
    transport_cost = budget - (trip_info[1] * budget)
    total_tickets_cost = (trip_info[category]) * people_count
elif people_count <= 9:
    transport_cost = budget - (trip_info[5] * budget)
    total_tickets_cost = (trip_info[category]) * people_count
elif people_count <= 24:
    transport_cost = budget - (trip_info[10] * budget)
    total_tickets_cost = (trip_info[category]) * people_count
elif people_count <= 49:
    transport_cost = budget - (trip_info[25] * budget)
    total_tickets_cost = (trip_info[category]) * people_count
elif people_count > 50:
    transport_cost = budget - (trip_info[50] * budget)
    total_tickets_cost = (trip_info[category]) * people_count

total = abs(total_tickets_cost - transport_cost)
if transport_cost >= total_tickets_cost:
    print(f"Yes! You have {total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total:.2f} leva.")
