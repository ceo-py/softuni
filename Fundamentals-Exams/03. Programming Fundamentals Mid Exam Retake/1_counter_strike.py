targets = [int(x) for x in input().split()]
shoot = input()
targets_len = len(targets)


while shoot != "End":
    shoot = int(shoot)

    if 0 <= shoot < targets_len:
        target = targets[shoot]
        targets[shoot] = -1
        for i in range(targets_len):

            if targets[i] == -1:
                continue

            if targets[i] > target:
                targets[i] -= target
            else:
                targets[i] += target

    shoot = input()

print(f"Shot targets: {sum(1 for x in targets if x == -1)} ->", *targets)







starting_energy = int(input())

command = input()
battle_wins_counter = 0
battle_won = True
while command != "End of battle":
    command = int(command)
    if starting_energy - command >= 0:
        battle_wins_counter += 1
        starting_energy += - command
    else:
        battle_won = False
        break
    if battle_wins_counter % 3 == 0:
        starting_energy += battle_wins_counter
    command = input()

if battle_won:
    print(f"Won battles: {battle_wins_counter}. Energy left: {starting_energy}")
else:
    print(f"Not enough energy! Game ends with {battle_wins_counter} won battles and {starting_energy} energy")
