days = int(input())
number_hours_for_every_day = int(input())

day_taxes = 0
day_tax = 0

for day in range(1, days + 1):
    day_tax = 0

    for hours in range(1, number_hours_for_every_day + 1):

        if day % 2 == 0 and hours % 2 != 0:
            day_taxes += 2.50
            day_tax += 2.50


        elif day % 2 != 0 and hours % 2 == 0:
            day_taxes += 1.25
            day_tax += 1.25

        else:
            day_taxes += 1
            day_tax += 1
            
    print(f"Day: {day} - {day_tax:.2f} leva")

print(f"Total: {day_taxes:.2f} leva")
