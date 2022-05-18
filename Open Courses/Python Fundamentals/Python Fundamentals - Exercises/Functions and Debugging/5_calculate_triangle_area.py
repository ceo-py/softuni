base = float(input())
height = float(input())


def calc_area(b, h):
    return f"{((b * h) / 2):.12g}"


print(calc_area(base, height))
