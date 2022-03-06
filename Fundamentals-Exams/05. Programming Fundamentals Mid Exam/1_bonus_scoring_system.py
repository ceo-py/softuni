import math
number_students = int(input())
number_lecturers = int(input())
additional_bonus = int(input())

max_bonus = 0
attendances_count = 0
for _ in range(number_students):
    attendances = int(input())
    score = (attendances / number_lecturers) * (5 + (additional_bonus))
    if max_bonus < score:
        max_bonus = score
        attendances_count = attendances

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {attendances_count} lectures.")
