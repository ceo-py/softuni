number_days = int(input())
hours_per_day = int(input())


total_tax = 0

for day in range(1, number_days + 1):
    day_tax = 0

    for hour in range(1, hours_per_day + 1):

        if day % 2 == 0 and hour % 2 != 0:
            total_tax += 2.50
            day_tax += 2.50

        elif day % 2 != 0 and hour % 2 == 0:
            total_tax += 1.25
            day_tax += 1.25
        else:
            total_tax += 1
            day_tax += 1

    print(f"Day: {day} - {day_tax:.2f} leva")

print(f"Total: {total_tax:.2f} leva")