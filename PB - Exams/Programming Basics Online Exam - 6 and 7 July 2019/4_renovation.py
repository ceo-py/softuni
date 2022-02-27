import math

height_walls = int(input())
width_walls = int(input())
surface_not_to_paint = int(input())

walls_total_surface = height_walls * width_walls * 4
wall_surface_to_paint = math.ceil(walls_total_surface - ((walls_total_surface * surface_not_to_paint) / 100))
is_wall_not_painted = True
while is_wall_not_painted:

    painted_surface = input()

    if painted_surface == "Tired!":
        print(f"{wall_surface_to_paint} quadratic m left.")
        is_wall_not_painted = False

    else:
        painted_surface = int(painted_surface)
        wall_surface_to_paint += - painted_surface

    if wall_surface_to_paint < 0:
        print(f"All walls are painted and you have {abs(wall_surface_to_paint)} l paint left!")
        is_wall_not_painted = False

    elif wall_surface_to_paint == 0:
        print(f"All walls are painted! Great job, Pesho!")
        is_wall_not_painted = False
