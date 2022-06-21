employee_info = [int(input()) for num in range(4)]
*total_answers_per_hour, students_in_q = employee_info
time_needed = 1
while students_in_q > 0:
    if time_needed % 4 != 0:
        students_in_q -= sum(total_answers_per_hour)
    time_needed += 1

print(f"Time needed: {time_needed - 1}h.")






#
#
#
# employee_one_efficiency = int(input())
# employee_two_efficiency = int(input())
# employee_three_efficiency = int(input())
# students_in_q = int(input())
#
# total_answers_per_hour = employee_one_efficiency + employee_two_efficiency + employee_three_efficiency
#
# time_needed = 0
# for hour in range(1, students_in_q + 1):
#     if hour % 4 != 0 and students_in_q > 0:
#         students_in_q += -total_answers_per_hour
#     elif students_in_q <= 0:
#         break
#     time_needed += 1
#
# print(f"Time needed: {time_needed}h.")
