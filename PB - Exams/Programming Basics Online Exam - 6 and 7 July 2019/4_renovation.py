import math

high_wall = int(input())
width_wall = int(input())
no_paint_wall_percent = int(input())

paint_lt = input()
total_room_size = math.ceil((high_wall * width_wall * 4) * (1 - no_paint_wall_percent / 100))


while paint_lt != 'Tired!':
    paint_lt = int(paint_lt)

    total_room_size -= paint_lt

    if total_room_size < 0:
        print(f'All walls are painted and you have {abs(total_room_size)} l paint left!')
        break

    if total_room_size == 0:
        print('All walls are painted! Great job, Pesho!')
        break

    paint_lt = input()

else:
    print(f'{total_room_size} quadratic m left.')






# import math
#
# height_walls = int(input())
# width_walls = int(input())
# surface_not_to_paint = int(input())
#
# walls_total_surface = height_walls * width_walls * 4
# wall_surface_to_paint = math.ceil(walls_total_surface - ((walls_total_surface * surface_not_to_paint) / 100))
# is_wall_not_painted = True
# while is_wall_not_painted:
#
#     painted_surface = input()
#
#     if painted_surface == "Tired!":
#         print(f"{wall_surface_to_paint} quadratic m left.")
#         is_wall_not_painted = False
#
#     else:
#         painted_surface = int(painted_surface)
#         wall_surface_to_paint -= painted_surface
#
#     if wall_surface_to_paint < 0:
#         print(f"All walls are painted and you have {abs(wall_surface_to_paint)} l paint left!")
#         is_wall_not_painted = False
#
#     elif wall_surface_to_paint == 0:
#         print(f"All walls are painted! Great job, Pesho!")
#         is_wall_not_painted = False





# from math import ceil
#
# height = int(input())
# width = int(input())
# percent_no_paint = int(input())
#
# is_tired = False
# total_walls = height * width * 4
# walls_for_painting = ceil(total_walls - ((total_walls * percent_no_paint) / 100))
# paintings_left = walls_for_painting
#
# while paintings_left <= walls_for_painting:
#     command = input()
#
#     if command == "Tired!":
#         is_tired = True
#         break
#
#     liters_of_paint = int(command)
#     paintings_left -= liters_of_paint
#
#     if paintings_left <= 0:
#         break
#
# if is_tired:
#     print(f"{paintings_left} quadratic m left.")
# elif paintings_left >= 0:
#     print("All walls are painted! Great job, Pesho!")
# else:
#     print(f"All walls are painted and you have {abs(paintings_left)} l paint left!")
