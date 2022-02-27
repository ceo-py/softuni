import datetime

time_first = int(input())
time_second = int(input())
time_third = int(input())

conversion = str(datetime.timedelta(seconds=time_first + time_second + time_third))
print(conversion[3:])
