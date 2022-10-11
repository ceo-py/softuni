initial_energy = int(input())
distance = input()
wins = 0

while distance != "End of battle":
    distance = int(distance)
    initial_energy -= distance

    if initial_energy < 0:
        print(f"Not enough energy! Game ends with {wins} won battles and {initial_energy + distance} energy")
        break

    wins += 1
    if wins % 3 == 0:
        initial_energy += wins

    distance = input()

else:
    print(f"Won battles: {wins}. Energy left: {initial_energy}")


#
# starting_energy = int(input())
#
# command = input()
# battle_wins_counter = 0
# battle_won = True
# while command != "End of battle":
#     command = int(command)
#     if starting_energy - command >= 0:
#         battle_wins_counter += 1
#         starting_energy += - command
#     else:
#         battle_won = False
#         break
#     if battle_wins_counter % 3 == 0:
#         starting_energy += battle_wins_counter
#     command = input()
#
# if battle_won:
#     print(f"Won battles: {battle_wins_counter}. Energy left: {starting_energy}")
# else:
#     print(f"Not enough energy! Game ends with {battle_wins_counter} won battles and {starting_energy} energy")
