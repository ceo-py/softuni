from collections import deque

bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = [int(x) for x in input().split(", ")]
full_set = False

bombs = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while bomb_effects and bomb_casings and not full_set:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()
    mix_effect = effect + casing
    for bomb, quantity in (("Datura Bombs", 40), ("Cherry Bombs", 60), ("Smoke Decoy Bombs", 120)):
        if mix_effect == quantity:
            bombs[bomb] += 1
            break
    else:
        bomb_casings.append(casing - 5)
        bomb_effects.appendleft(effect)
    if all(x >= 3 for x in bombs.values()):
        full_set = True

if full_set:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")

for bomb, quantity in bombs.items():
    print(f"{bomb}: {quantity}")