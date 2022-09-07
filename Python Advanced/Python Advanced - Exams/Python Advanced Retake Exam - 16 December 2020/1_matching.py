from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())
matches = 0


while males and females:
    if females[0] <= 0:
        del females[0]
        continue
    if females[0] % 25 == 0:
        del females[0]
        del females[0]
        continue
    if males[-1] <= 0:
        del males[-1]
        continue
    if males[-1] % 25 == 0:
        del males[-1]
        del males[-1]
        continue
    female = females.popleft()
    male = males.pop()
    if female == male:
        matches += 1
        continue
    males.append(male - 2)

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(str(x) for x in males[::-1])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")