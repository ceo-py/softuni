import math

number_balls = int(input())
ball_color = list()
i = 0
while True:
    ball = input()
    ball_color.append(ball)
    i = i + 1
    if number_balls == i:
        break
red_balls_counter = 0
orange_balls_counter = 0
yellow_balls_counter = 0
white_balls_counter = 0
black_balls_counter = 0
other_balls_counter = 0
black_balls_points = list()
total_points = 0

for balls in ball_color:
    if "red" in balls:
        total_points += 5
        red_balls_counter += 1
    elif "orange" in balls:
        total_points += 10
        orange_balls_counter += 1
    elif "yellow" in balls:
        total_points += 15
        yellow_balls_counter += 1
    elif "white" in balls:
        total_points += 20
        white_balls_counter += 1
    elif "black" in balls:
        black_balls_counter += 1
        total_points = math.floor(total_points / 2)
        black_balls_points.append(black_balls_counter)
    else:
        other_balls_counter += 1

total_points = "{:.0f}".format(total_points)
print(f"Total points: {total_points}")
print(f"Red balls: {red_balls_counter}")
print(f"Orange balls: {orange_balls_counter}")
print(f"Yellow balls: {yellow_balls_counter}")
print(f"White balls: {white_balls_counter}")
print(f"Other colors picked: {other_balls_counter}")
print(f"Divides from black balls: {black_balls_counter}")
