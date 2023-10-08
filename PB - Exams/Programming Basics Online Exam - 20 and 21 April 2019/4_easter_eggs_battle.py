player_one_eggs = int(input())
player_two_eggs = int(input())
command = input()

while command != 'End':
    if command == 'one':
        player_two_eggs -= 1
        if player_two_eggs == 0:
            print(f'Player two is out of eggs. Player one has {player_one_eggs} eggs left.')
            break

    elif command == 'two':
        player_one_eggs -= 1
        if player_one_eggs == 0:
            print(f'Player one is out of eggs. Player two has {player_two_eggs} eggs left.')
            break

    command = input()

else:
    print(f'Player one has {player_one_eggs} eggs left.')
    print(f'Player two has {player_two_eggs} eggs left.')







# player_one_eggs = int(input())
# player_two_eggs = int(input())
#
# player_one_eggs_left = player_one_eggs
# player_two_eggs_left = player_two_eggs
#
# while True:
#     winner = input()
#     if winner == "End of battle":
#         print(f"Player one has {player_one_eggs_left} eggs left.\nPlayer two has {player_two_eggs_left} eggs left.")
#         break
#
#     if winner == "one":
#         player_two_eggs_left -= 1
#
#     else:
#         player_one_eggs_left -= 1
#
#     if player_one_eggs_left == 0:
#         print(f"Player one is out of eggs. Player two has {player_two_eggs_left} eggs left.")
#         break
#
#     elif player_two_eggs_left == 0:
#         print(f"Player two is out of eggs. Player one has {player_one_eggs_left} eggs left.")
#         break