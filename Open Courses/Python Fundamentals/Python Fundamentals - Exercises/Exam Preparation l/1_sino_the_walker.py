import time

time_sino = input()
number_steps = int(input())
time_interval_steps = int(input())
t = tuple(time_sino)
time_format = "%H:%M:%S"
a = time.strptime(time_sino, time_format)
print(f"{a.tm_hour}:{a.tm_min}:{a.tm_sec}")
convert_hours = (number_steps * time_interval_steps)/60
convert_min = (number_steps * time_interval_steps)//60
convert_sec = (number_steps * time_interval_steps)%60

b = time.strptime(time_sino, time_format)

