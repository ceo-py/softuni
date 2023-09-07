from math import ceil

movie = str(input())
movie_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
relax_time = break_time / 4

available_time = break_time - lunch_time - relax_time
diff = abs(movie_time - available_time)

if movie_time > available_time:
    print(f"You don't have enough time to watch {movie}, you need {ceil(diff)} more minutes.")
else:
    print(f"You have enough time to watch {movie} and left with {ceil(diff)} minutes free time.")






# import math
#
# name_serial = input()
# serial_len = int(input())
# break_time = int(input())
#
# time_for_lunch = break_time * 1 / 8
# time_for_rest = break_time * 1 / 4
# time_left = break_time - time_for_lunch - time_for_rest
#
# if serial_len <= time_left:
#     time_left = time_left - serial_len
#     print(f"You have enough time to watch {name_serial} "
#           f"and left with {math.ceil(time_left)} minutes free time.")
# else:
#     time_left = serial_len - time_left
#     print(f"You don't have enough time to watch {name_serial}, "
#           f"you need {math.ceil(time_left)} more minutes.")
