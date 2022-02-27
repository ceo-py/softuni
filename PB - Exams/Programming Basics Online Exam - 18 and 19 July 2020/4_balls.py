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

balls = {"points": {
    "red": 0,
    "orange": 0,
    "yellow": 0,
    "white": 0,
    "black": 0,
    "total points": 0},
    "counter": {
        "red": 0,
        "orange": 0,
        "yellow": 0,
        "white": 0,
        "black": 0,
        "other balls": 0,
    },
    "bonus points": {
        "red": 5,
        "orange": 10,
        "yellow": 15,
        "white": 20,
        "black": 0,
    },

}
color_check = ("red", "orange", "yellow", "white", "black")

for ball in ball_color:

    if "black" in ball:
        balls["points"]["total points"] = math.floor(balls["points"]["total points"] / 2)

    if ball not in color_check:
        balls["counter"]["other balls"] += 1

    else:
        balls["points"]["total points"] += balls["bonus points"][ball]
        balls["counter"][ball] += 1

total_points = "{:.0f}".format(balls["points"]["total points"])
print(f"Total points: {total_points}")
print("Red balls:", balls["counter"]["red"])
print("Orange balls:", balls["counter"]["orange"])
print("Yellow balls:", balls["counter"]["yellow"])
print("White balls:", balls["counter"]["white"])
print("Other colors picked:", balls["counter"]["other balls"])
print("Divides from black balls:", balls["counter"]["black"])
