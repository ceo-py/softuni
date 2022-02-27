house_height = float(input())
house_length = float(input())
wall_of_the_roof_height = float(input())


windows = 2.25
door = 2.4
green_paint = 3.4
red_paint = 4.3

# walls
side_wall = house_height * house_length
side_wall_total = (side_wall * 2) - (windows * 2)
back_wall = ((house_height * house_height) * 2) - door
total_area_walls = side_wall_total + back_wall
green_paint_needed = total_area_walls / green_paint

#roof
two_rectangle_roof = 2 * (house_height * house_length)
two_triangle_roof = 2 * (house_height * wall_of_the_roof_height / 2)
total_area_roof = two_rectangle_roof + two_triangle_roof
red_paint_needed = total_area_roof / red_paint



print(f"{green_paint_needed:.2f}")
print(f"{red_paint_needed:.2f}")
