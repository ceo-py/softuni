import math

name_serial = input()
serial_len = int(input())
break_time = int(input())

time_for_lunch = break_time * 1 / 8
time_for_rest = break_time * 1 / 4
time_left = break_time - time_for_lunch - time_for_rest

if serial_len <= time_left:
    time_left = time_left - serial_len
    print(f"You have enough time to watch {name_serial} "
          f"and left with {math.ceil(time_left)} minutes free time.")
else:
    time_left = serial_len - time_left
    print(f"You don't have enough time to watch {name_serial}, "
          f"you need {math.ceil(time_left)} more minutes.")
