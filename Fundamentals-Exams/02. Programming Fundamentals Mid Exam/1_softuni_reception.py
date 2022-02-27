employee_one_efficiency = int(input())
employee_two_efficiency = int(input())
employee_three_efficiency = int(input())
students_in_q = int(input())

total_answers_per_hour = employee_one_efficiency + employee_two_efficiency + employee_three_efficiency

time_needed = 0
for hour in range(1, students_in_q + 1):
    if hour % 4 != 0 and students_in_q > 0:
        students_in_q += -total_answers_per_hour
    elif students_in_q <= 0:
        break
    time_needed += 1

print(f"Time needed: {time_needed}h.")
