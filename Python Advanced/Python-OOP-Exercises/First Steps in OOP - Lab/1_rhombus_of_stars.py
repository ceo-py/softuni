number_of_rhombus = int(input())


class Rhombus:
    def __init__(self, stars):
        self.stars = stars
        self.draw = []

    def make_rhombus(self):
        for row in range(1, self.stars + 1):
            if row == 1:
                self.draw.append((self.stars - row) * " " + row * "*")
            else:
                self.draw.append((self.stars - row) * " " + row * "* ")
        for rows in range(0, self.stars - 1):
            if rows == 0:
                self.draw.append((self.stars - (row - 1)) * " " + (self.stars - 1) * "* ")
            else:
                self.draw.append((rows + 1) * " " + (self.stars - rows - 1) * "* ")

    def __repr__(self):
        return '\n'.join(self.draw)


r = Rhombus(number_of_rhombus)
r.make_rhombus()
print(r)









#
#
#
# number_of_rhombus = int(input())
#
#
# class Rhombus:
#     def __init__(self, stars):
#         self.stars = stars
#
#     def show_result(self):
#         for row in range(1, self.stars + 1):
#             if row == 1:
#                 print((self.stars - row) * " " + row * "*")
#             else:
#                 print((self.stars - row) * " " + row * "* ")
#         for rows in range(0, self.stars - 1):
#             if rows == 0:
#                 print((self.stars - (row - 1)) * " " + (self.stars - 1) * "* ")
#             else:
#                 print((rows + 1) * " " + (self.stars - rows - 1) * "* ")
#
#
# r = Rhombus(number_of_rhombus)
# r.show_result()
