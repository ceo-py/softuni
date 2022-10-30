class ImageArea:

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def __lt__(self, obj):
        return self.get_area() < obj.get_area()

    def __le__(self, obj):
        return self.get_area() <= obj.get_area()

    def __eq__(self, obj):
        return self.get_area() == obj.get_area()

    def __ne__(self, obj):
        return self.get_area() != obj.get_area()

    def __gt__(self, obj):
        return self.get_area() > obj.get_area()

    def __ge__(self, obj):
        return self.get_area() >= obj.get_area()

# check https://docs.python.org/3/reference/datamodel.html
# for for info