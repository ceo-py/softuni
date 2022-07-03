from _collections import deque

duration_green = int(input())
window = int(input())
line = input()
cars = deque()
cars_counter = 0
crashed = False

while line != "END":
    if line == "green":
        if cars:
            current_car = cars.popleft()
            left_seconds = duration_green - len(current_car)

            while left_seconds > 0:
                cars_counter += 1
                if not cars:
                    break
                current_car = cars.popleft()
                left_seconds -= len(current_car)

            if left_seconds == 0:
                cars_counter += 1
            if window >= abs(left_seconds):
                if left_seconds < 0:
                    cars_counter += 1
            else:
                index = window + left_seconds
                print(f"A crash happened!\n{current_car} was hit at {current_car[index]}.")
                crashed = True
                break
    else:
        cars.append(line)
    line = input()

if not crashed:
    print(f"Everyone is safe.\n{cars_counter} total cars passed the crossroads.")






#
#
# from collections import deque
#
# green_lift_duration = int(input())
# free_window_in_sec = int(input())
# car_or_command = input()
#
# car_q = deque()
# passed_cars = 0
#
# while car_or_command != "END":
#     if car_or_command != "green":
#         car_q.append(car_or_command)
#     else:
#         if car_q:
#             green_lift_start = green_lift_duration
#             free_window_on_gree = free_window_in_sec
#             for _ in range(len(car_q)):
#                 car_enter = False
#                 car = car_q.popleft()
#                 coming_tru_car = len(car)
#                 if green_lift_start != 0:
#                     green_lift_start -= coming_tru_car
#                     car_enter = True
#                 if green_lift_start < 0:
#                     coming_tru_car = abs(green_lift_start)
#                     green_lift_start = 0
#                 else:
#                     passed_cars += 1
#                     continue
#                 if coming_tru_car and car_enter:
#                     coming_tru_car -= free_window_on_gree
#                     if coming_tru_car > 0:
#                         print(f"A crash happened!\n{car} was hit at {list(car)[-coming_tru_car]}.")
#                         exit()
#                     passed_cars += 1
#                     break
#
#     car_or_command = input()
#
# print(f"Everyone is safe.\n{passed_cars} total cars passed the crossroads.")
#
#
#
#
#
#
#















