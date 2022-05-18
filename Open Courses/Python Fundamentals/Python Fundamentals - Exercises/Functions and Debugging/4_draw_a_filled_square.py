n = int(input())


def draw_first_last_line(n):
    print(f"{(n + n) * '-'}")


def draw_middle(n):
    n = n - 1
    m = "\/"
    text = f"-{n * m}-"
    for _ in range(1, n):
        print(text)


draw_first_last_line(n)
draw_middle(n)
draw_first_last_line(n)
