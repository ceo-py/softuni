off_days = int(input())

days_in_year = 365
petting_per_working_day = 63
petting_per_off_day = 127
norm_for_play_time = 30000
working_days = (days_in_year - off_days) * petting_per_working_day

real_time_petting = working_days + off_days * petting_per_off_day

diffrence_between_pay_time = abs(norm_for_play_time - real_time_petting)
total_time_hours = diffrence_between_pay_time // 60
total_time_minutes = diffrence_between_pay_time % 60

if norm_for_play_time > real_time_petting:
    print(f"Tom sleeps well\n"
          f"{total_time_hours} hours and {total_time_minutes} minutes less for play")
else:
    total = abs(real_time_petting - norm_for_play_time)
    total_time_hours = total // 60
    total_time_minutes = total % 60
    print(f"Tom will run away\n"
          f"{total_time_hours} hours and {total_time_minutes} minutes more for play")
