class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = float(radius)

    def set_radius(self, new_radius):
        self.radius = float(new_radius)

    def get_area(self):
        return Circle.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * Circle.pi * self.radius
