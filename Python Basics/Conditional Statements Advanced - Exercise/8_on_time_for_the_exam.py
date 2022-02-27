hour_on_examp = int(input())
min_on_examp = int(input())
hour_on_arrival = int(input())
min_on_arrival = int(input())

exam_time = (hour_on_examp * 60) + min_on_examp
arrival_time = (hour_on_arrival * 60) + min_on_arrival

time_left = (exam_time - arrival_time) / 60
min_left = (exam_time - arrival_time) % 60

if exam_time == arrival_time:
    print("On time")
elif min_left > 30:
    time_type = "Early"
else:
    time_type = "On time"
if min_left == 0:
    min_left = 00
number_chekc = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

check_under_zero_time = str(time_left)

if check_under_zero_time[0] == '-' and check_under_zero_time[1] in number_chekc:
    min_left = (arrival_time - exam_time) % 60
    time_left = abs(time_left)
    print(f"Late\n{int(time_left)}:{min_left:02d} hours after the start")
elif exam_time > arrival_time and time_left < 1:
    time_left = (exam_time - arrival_time)
    print(f"{time_type}\n{time_left} minutes before the start")
elif exam_time < arrival_time and time_left < 1:
    time_left = (arrival_time - exam_time)
    print(f"Late\n{time_left} minutes after the start")
elif exam_time > arrival_time and time_left >= 1:
    time_left = (exam_time - arrival_time) / 60
    print(f"Early\n{int(time_left)}:{min_left:02d} hours before the start")
elif exam_time < arrival_time and time_left <= 1:
    time_left = (arrival_time - exam_time) / 60
    print(f"Late\n{int(time_left)}:{min_left:02d} minutes after the start")
