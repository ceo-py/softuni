import math
n = int(input())


for roof in range(math.ceil(n / 2)):
    if roof == 0:
        if n % 2 == 0:
            stars = 2
        else:
            stars = 1
        lines = int((n - stars) / 2)
    else:
        stars += 2
        lines -= 1
    print(lines * "-" + stars * "*" + lines * "-")

for base in range(int(n/2)):
    stars = n - 2
    print("|" + stars * "*" + "|")