import math

points = []


class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def CalcDistance(self, p1, p2):
        side_a = int(p1[0]) - int(p2[0])
        side_b = int(p1[-1]) - int(p2[-1])
        total = math.sqrt(side_a ** 2 + side_b ** 2)
        return total

    def find_closest_points(self, points_):
        result_ = 100_000_000
        x_num = ""
        y_num = ""
        for i in range(len(points_)):
            for j in range(i + 1, len(points_)):
                check = p.CalcDistance(points_[i], points_[j])
                if check < result_:
                    result_ = check
                    x_num = points_[i]
                    y_num = points_[j]
        return result_, x_num, y_num


p = Point()
for _ in range(int(input())):
    points.append(input().split())

result, x_num, y_num = p.find_closest_points(points)
print(f"{result:.3f}")
print(f"({', '.join(x_num)})")
print(f"({', '.join(y_num)})")
