from math import sqrt


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def calc_distance(self):
        return sqrt((self.x[0] - self.y[0]) ** 2
                    + (self.x[1] - self.y[1]) ** 2)


class Box:
    box_data = []

    def __init__(self, _tl, _tr, _bl, _br):
        self.width = None
        self.height = None
        self.perimeter = None
        self.area = None
        self.tl = _tl
        self.tr = _tr
        self.bl = _bl
        self.br = _br

    def CalculatePerimeter(self):
        self.width = int(Point(self.tl, self.tr).calc_distance())
        self.height = int(Point(self.tl, self.bl).calc_distance())

    def CalculateArea(self):
        self.perimeter = int(self.width * 2 + self.height * 2)
        self.area = int(self.width * self.height)

    def __repr__(self):
        return f"Box: {box.width}, {box.height}\nPerimeter: {box.perimeter}\nArea: {box.area}"


data = input()
while data != "end":
    top_l = [int(i) for i in data.split(" | ")[0].split(":")]
    top_r = [int(i) for i in data.split(" | ")[1].split(":")]
    bottom_l = [int(i) for i in data.split(" | ")[2].split(":")]
    bottom_r = [int(i) for i in data.split(" | ")[3].split(":")]
    Box.box_data.append(Box(top_l, top_r, bottom_l, bottom_r))
    data = input()

for box in Box.box_data:
    box.CalculatePerimeter()
    box.CalculateArea()
    print(box)
