days, daily_plunder, expected_plunder = int(input()), int(input()), float(input())

total_plunder = 0

for day in range(1, days + 1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += (daily_plunder * 0.50)
    if day % 5 == 0:
        total_plunder -= (total_plunder * 0.30)

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percent_left = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percent_left:.2f}% of the plunder.")
