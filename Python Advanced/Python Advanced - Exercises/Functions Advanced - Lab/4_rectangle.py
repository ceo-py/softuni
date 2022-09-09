# def rectangle(*args):
#     # if any([True for x in args if not isinstance(x, int)]):
#
#     if not all([True if isinstance(x, int) else False for x in args]):
#         return "Enter valid values!"
#
#     def area():
#         return args[0] * args[1]
#
#     def perimeter():
#         return (args[0] + args[1]) * 2
#
#     return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
#


def rectangle(length, width):
    if not all([isinstance(x, int) for x in [length, width]]):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return (length + width) * 2

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"




print(rectangle(2, 10))
print(rectangle('2', 10))
