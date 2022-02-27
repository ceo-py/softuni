import math

hours_need_for_project = int(input())
days_firm_has_project = int(input())
number_employees_working_over_time = int(input())

normal_working_day = 8
employees_allow_over_time = 2
time_for_training = 0.10
total_working_hours = (days_firm_has_project - (days_firm_has_project * time_for_training)) * normal_working_day
employees_working_over_time = (number_employees_working_over_time * (employees_allow_over_time * days_firm_has_project))
total_hours_check = abs(total_working_hours + employees_working_over_time)
total_hours = abs((total_working_hours + employees_working_over_time) - hours_need_for_project)

if hours_need_for_project <= total_hours_check:
    print(f"Yes!{math.floor(total_hours)} hours left.")
else:
    print(f"Not enough time!{math.ceil(total_hours)} hours needed.")
