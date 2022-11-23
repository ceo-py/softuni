import datetime as dt

leaving_time_input = input()
steps = int(input())
secs_per_step = int(input())
seconds = (steps * secs_per_step)
seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
steps_time = dt.datetime(1, 1, 1, hour, minutes, seconds)


t1 = dt.datetime.strptime("".join(str(x) for x in leaving_time_input), '%H:%M:%S')
t2 = dt.datetime.strptime("".join(str(x) for x in str(steps_time).split()[1]), '%H:%M:%S')
time_zero = dt.datetime.strptime('00:00:00', '%H:%M:%S')
print(f"Time Arrival: {(t1 - time_zero + t2).time()}")