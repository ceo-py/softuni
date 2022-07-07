figures = int(input())


def recursive_drawing(figures):
    if figures <= 0:
        return
    print("*" * figures)
    recursive_drawing(figures - 1)
    print("#" * figures)


recursive_drawing(figures)