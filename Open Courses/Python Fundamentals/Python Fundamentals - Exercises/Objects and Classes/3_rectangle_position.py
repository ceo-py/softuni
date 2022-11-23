rectangle = []


class Point:
    def __init__(self, left: int, top: int, width: int, height: int):
        self.top = int(top)
        self.left = int(left)
        self.width = int(width)
        self.height = int(height)
        self.right = self.left + self.width
        self.bottom = self.height - self.top

    def is_inside(self, rectangle_):
        if self.left >= rectangle_.left \
                and self.right <= rectangle_.right \
                and self.top <= rectangle_.top \
                and self.bottom <= rectangle_.bottom:
            return "Inside"

        return "Not inside"


r1 = Point(*input().split())
r2 = Point(*input().split())

print(r1.is_inside(r2))
