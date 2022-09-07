from collections import deque

fire_work_effects = deque(int(x) for x in input().split(", "))
explosive_power = [int(x) for x in input().split(", ")]

fireworks = {
    "Palm": 0,
    "Willow": 0,
    "Crossette": 0,
    "Enough" : False
}

while fire_work_effects and explosive_power and not fireworks["Enough"]:
    if fire_work_effects[0] <= 0:
        del fire_work_effects[0]
        continue
    if explosive_power[-1] <= 0:
        del explosive_power[-1]
        continue
    effect = fire_work_effects.popleft()
    power = explosive_power.pop()
    mix_sum = effect + power
    if mix_sum % 5 == 0 and mix_sum % 3 == 0:
        fireworks["Crossette"] += 1
    elif mix_sum % 5 == 0:
        fireworks["Willow"] += 1
    elif mix_sum % 3 == 0:
        fireworks["Palm"] += 1
    else:
        fire_work_effects.append(effect - 1)
        explosive_power.append(power)
    if all(x >= 3 for x in list(fireworks.values())[:3]):
        fireworks["Enough"] = True

if fireworks["Enough"]:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fire_work_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in fire_work_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")
for firework, quantity in list(fireworks.items())[:3]:
    print(f"{firework} Fireworks: {quantity}")
