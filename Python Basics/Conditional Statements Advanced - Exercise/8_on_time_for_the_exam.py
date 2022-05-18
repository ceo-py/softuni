hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

time_for_exam = hour_of_exam * 60 + minutes_of_exam
time_for_arrival = hour_of_arrival * 60 + minutes_of_arrival
diff = abs(time_for_exam - time_for_arrival)
hour = diff // 60
minutes = diff % 60
if time_for_exam == time_for_arrival:
    print('On Time')

elif time_for_arrival > time_for_exam:
    print('Late')
    if diff > 59:
        print(f'{hour}:{minutes:02d} hours after the start')
    else:
        print(f'{minutes} minutes after the start')
elif time_for_arrival < time_for_exam:
    if diff <= 30:
        print('On time')
        print(f'{diff} minutes before the start')
    else:
        print('Early')
        if diff > 59:
            print(f'{hour}:{minutes:02d} hours before the start')
        else:
            print(f'{minutes} minutes before the start')

#
#
#
# hour_on_examp = int(input())
# min_on_examp = int(input())
# hour_on_arrival = int(input())
# min_on_arrival = int(input())
#
# exam_time = (hour_on_examp * 60) + min_on_examp
# arrival_time = (hour_on_arrival * 60) + min_on_arrival
#
# time_left = (exam_time - arrival_time) / 60
# min_left = (exam_time - arrival_time) % 60
#
# if exam_time == arrival_time:
#     print("On time")
# elif min_left > 30:
#     time_type = "Early"
# else:
#     time_type = "On time"
# if min_left == 0:
#     min_left = 00
# number_chekc = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
#
# check_under_zero_time = str(time_left)
#
# if check_under_zero_time[0] == '-' and check_under_zero_time[1] in number_chekc:
#     min_left = (arrival_time - exam_time) % 60
#     time_left = abs(time_left)
#     print(f"Late\n{int(time_left)}:{min_left:02d} hours after the start")
# elif exam_time > arrival_time and time_left < 1:
#     time_left = (exam_time - arrival_time)
#     print(f"{time_type}\n{time_left} minutes before the start")
# elif exam_time < arrival_time and time_left < 1:
#     time_left = (arrival_time - exam_time)
#     print(f"Late\n{time_left} minutes after the start")
# elif exam_time > arrival_time and time_left >= 1:
#     time_left = (exam_time - arrival_time) / 60
#     print(f"Early\n{int(time_left)}:{min_left:02d} hours before the start")
# elif exam_time < arrival_time and time_left <= 1:
#     time_left = (arrival_time - exam_time) / 60
#     print(f"Late\n{int(time_left)}:{min_left:02d} minutes after the start")
