number_of_rhombus = int(input())


class Rhombus:
    def __init__(self, stars):
        self.stars = stars

    def show_result(self):
        for row in range(1, self.stars + 1):
            if row == 1:
                print((self.stars - row) * " " + row * "*")
            else:
                print((self.stars - row) * " " + row * "* ")
        for rows in range(0, self.stars - 1):
            if rows == 0:
                print((self.stars - (row - 1)) * " " + (self.stars - 1) * "* ")
            else:
                print((rows + 1) * " " + (self.stars - rows - 1) * "* ")


r = Rhombus(number_of_rhombus)
r.show_result()
