ball_numbers = int(input())

total_points = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
other = 0

for turn in range(ball_numbers):
    ball = input()

    if ball == "red":
        red += 1
        total_points += 5

    elif ball == "orange":
        orange += 1
        total_points += 10

    elif ball == "yellow":
        yellow += 1
        total_points += 15

    elif ball == "white":
        white += 1
        total_points += 20

    elif ball == "black":
        black += 1
        total_points = int(total_points / 2)

    else:
        other += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")




#
# import math
#
# number_balls = int(input())
# ball_color = list()
# i = 0
# while True:
#     ball = input()
#     ball_color.append(ball)
#     i = i + 1
#     if number_balls == i:
#         break
#
# balls = {"points": {
#     "red": 0,
#     "orange": 0,
#     "yellow": 0,
#     "white": 0,
#     "black": 0,
#     "total points": 0},
#     "counter": {
#         "red": 0,
#         "orange": 0,
#         "yellow": 0,
#         "white": 0,
#         "black": 0,
#         "other balls": 0,
#     },
#     "bonus points": {
#         "red": 5,
#         "orange": 10,
#         "yellow": 15,
#         "white": 20,
#         "black": 0,
#     },
#
# }
# color_check = ("red", "orange", "yellow", "white", "black")
#
# for ball in ball_color:
#
#     if "black" in ball:
#         balls["points"]["total points"] = math.floor(balls["points"]["total points"] / 2)
#
#     if ball not in color_check:
#         balls["counter"]["other balls"] += 1
#
#     else:
#         balls["points"]["total points"] += balls["bonus points"][ball]
#         balls["counter"][ball] += 1
#
# total_points = "{:.0f}".format(balls["points"]["total points"])
# print(f"Total points: {total_points}")
# print("Red balls:", balls["counter"]["red"])
# print("Orange balls:", balls["counter"]["orange"])
# print("Yellow balls:", balls["counter"]["yellow"])
# print("White balls:", balls["counter"]["white"])
# print("Other colors picked:", balls["counter"]["other balls"])
# print("Divides from black balls:", balls["counter"]["black"])
#



# import math
#
# ball_numbers = int(input())
#
# total_points = 0
# ball_red = 0
# ball_orange = 0
# ball_yellow = 0
# ball_white = 0
# other_colors = 0
# divided_black = 0
#
# for ball in range(ball_numbers):
#     ball_color = input()
#
#     if ball_color == 'red':
#         total_points += 5
#         ball_red += 1
#
#     elif ball_color == 'orange':
#         total_points += 10
#         ball_orange += 1
#
#     elif ball_color == 'yellow':
#         total_points += 15
#         ball_yellow += 1
#
#     elif ball_color == 'white':
#         total_points += 20
#         ball_white += 1
#
#     elif ball_color == 'black':
#         divided_black += 1
#         total_points -= math.ceil(total_points / 2)
#
#     else:
#         other_colors += 1
#
# print(f'Total points: {total_points}')
# print(f'Red balls: {ball_red}')
# print(f'Orange balls: {ball_orange}')
# print(f'Yellow balls: {ball_yellow}')
# print(f'White balls: {ball_white}')
# print(f'Other colors picked: {other_colors}')
# print(f'Divides from black balls: {divided_black}')

