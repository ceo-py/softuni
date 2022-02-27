import math

n = int(input())
lines = math.ceil((n - 1) / 2)
mid = 0
z = 0
if n % 2 == 0:
    lines = lines - 1
    z = 1
for i in range(1, lines + 2):
    if i == 1:
        if n % 2 == 0:
            lines = int(abs(2 - n) / 2)
            stars = 2
            print(lines * "-" + stars * "*" + lines * "-")
        else:
            lines = int(abs(n - 1) / 2)
            stars = 1
            print(lines * "-" + stars * "*" + lines * "-")
    if i > 1:
        if n % 2 == 0:
            mid += 2
        else:
            if mid == 0:
                mid += 1
            else:
                mid += 2
        lines = lines - 1

        print(lines * "-" + "*" + mid * "-" + "*" + lines * "-")

for b in range(0, math.floor(n / 2) - z):
    if n % 2 != 0:
        if b == math.floor(n / 2) - 1:
            lines = b + 1
            print(lines * "-" + "*" + lines * "-")
        else:
            lines = b + 1
            mid = mid - 2
            print(lines * "-" + "*" + mid * "-" + "*" + lines * "-")
    else:
        if b == math.floor(n / 2) - 1:
            lines = b + 1
            print(lines * "-" + "**" + lines * "-")
        else:
            lines = b + 1
            mid = mid - 2
            print(lines * "-" + "*" + mid * "-" + "*" + lines * "-")


