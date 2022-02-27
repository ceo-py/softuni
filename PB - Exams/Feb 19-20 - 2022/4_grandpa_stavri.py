days_boling_rakia = int(input())

rakia_total = 0
rakia_degreece = 0

for _ in range(days_boling_rakia):
    rakia = int(input())
    degrees = int(input())
    rakia_total += rakia
    rakia_degreece += rakia * degrees

average_degrees_of_rakia = rakia_degreece / rakia_total

print(f"Liter: {rakia_total:.2f}")
print(f"Degrees: {average_degrees_of_rakia:.2f}")

if 38 > average_degrees_of_rakia:
    print("Not good, you should baking!")
elif 42 > average_degrees_of_rakia:
    print("Super!")
else:
    print("Dilution with distilled water!")
