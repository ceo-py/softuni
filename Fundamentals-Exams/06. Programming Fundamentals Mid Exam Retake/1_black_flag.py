days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

current_plunder = 0


for day in range(1, days + 1):
    fifth_day = 1
    third_day = 0
    if day % 3 == 0:
        third_day = daily_plunder * 0.50
    if day % 5 == 0:
        fifth_day = 0.70

    current_plunder = (daily_plunder + current_plunder + third_day) * fifth_day

if current_plunder >= expected_plunder:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(current_plunder / expected_plunder) * 100:.2f}% of the plunder.")



#
#
# days, daily_plunder, expected_plunder = int(input()), int(input()), float(input())
#
# total_plunder = 0
#
# for day in range(1, days + 1):
#     total_plunder += daily_plunder
#     if day % 3 == 0:
#         total_plunder += (daily_plunder * 0.50)
#     if day % 5 == 0:
#         total_plunder -= (total_plunder * 0.30)
#
# if total_plunder >= expected_plunder:
#     print(f"Ahoy! {total_plunder:.2f} plunder gained.")
# else:
#     percent_left = (total_plunder / expected_plunder) * 100
#     print(f"Collected only {percent_left:.2f}% of the plunder.")
