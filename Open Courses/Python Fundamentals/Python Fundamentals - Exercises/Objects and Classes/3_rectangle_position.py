rectangle = []


class Point:
    def __init__(self, top, left, width, height):
        self.top = int(top)
        self.left = int(left)
        self.width = int(width)
        self.height = int(height)


    @staticmethod
    def is_inside(rectangle_):
        print(rectangle_[1].top)
        if all([rectangle_[0].left >= rectangle_[1].left, rectangle_[0].right <= rectangle_[1].right,
                rectangle_[0].top <= rectangle_[1].top, rectangle_[0].bottom <= rectangle_[1].bottom]):
            return "Inside"
        else:
            return "Not Inside"


for _ in range(2):
    top, left, width, height = input().split()
    rectangle.append(Point(top, left, width, height))

print(Point.is_inside(rectangle))
