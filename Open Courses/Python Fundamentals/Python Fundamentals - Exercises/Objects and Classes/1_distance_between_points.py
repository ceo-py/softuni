import math

point = []


class Point:
    def __init__(self, x, y):
        self.x = x.split()
        self.y = y.split()

    @staticmethod
    def CalcDistance(p1, p2):
        side_a = int(p1[0]) - int(p2[0])
        side_b = int(p1[-1]) - int(p2[-1])
        total = math.sqrt(side_a ** 2 + side_b ** 2)
        return f"{total:.3f}"


x = input()
y = input()
point.append(Point(x, y))

for show in point:
    print(Point.CalcDistance(show.x, show.y))
