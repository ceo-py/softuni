from collections import deque

milligrams_caffeine = deque(int(x) for x in input().split(", "))
energy_drinks = deque(int(x) for x in input().split(", "))
starting = 0

while milligrams_caffeine and energy_drinks:

    caffeine = milligrams_caffeine.pop()
    drink = energy_drinks.popleft()
    total_sum = caffeine * drink

    if starting + total_sum <= 300:
        starting += total_sum
        continue

    else:
        energy_drinks.append(drink)
        starting -= 30
        if starting < 0:
            starting = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {starting} mg caffeine.")

