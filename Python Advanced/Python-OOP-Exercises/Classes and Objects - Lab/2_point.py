class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def set_x(self, new_x):
        self.x = int(new_x)

    def set_y(self, new_y):
        self.y = int(new_y)

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"
