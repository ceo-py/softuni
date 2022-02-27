location = int(input())

for _ in range(location):
    target_gold = float(input())
    days_for_digging = int(input())
    total_for_location = 0
    for day in range(1, days_for_digging + 1):
        gold_digging = float(input())
        total_for_location += gold_digging
    average_gold = total_for_location / day
    if average_gold >= target_gold:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        needed_gold = abs(average_gold - target_gold)
        print(f"You need {needed_gold:.2f} gold.")
