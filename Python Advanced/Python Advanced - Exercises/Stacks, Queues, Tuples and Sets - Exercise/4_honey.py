from collections import deque

bees = deque(int(x) for x in input().split())
nectars = [int(x) for x in input().split()]
operations = deque(input().split())

honey_made = 0
operators = {
    "+": lambda f, s: f + s,
    "-": lambda f, s: f - s,
    "*": lambda f, s: f * s,
    "/": lambda f, s: f / s
}

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar < bee:
        bees.appendleft(bee)
        continue
    operation = operations.popleft()
    if nectar > 0:
        honey_made += abs(operators[operation](bee, nectar))

print(f"Total honey made: {honey_made}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")