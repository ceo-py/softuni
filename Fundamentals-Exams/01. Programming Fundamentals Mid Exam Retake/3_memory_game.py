main_string = [n for n in input().split()]
command = input()
move = 0
winner = False
while command != "end":
    command = command.split()
    index_one = int(command[0])
    index_two = int(command[-1])
    move += 1
    if index_two == index_one or index_two < 0 or index_one < 0 \
            or len(main_string) - 1 < index_one or len(main_string) - 1 < index_two:
        how_long = int(len(main_string) / 2)
        main_string.insert(how_long, (str(-move) + "a"))
        main_string.insert(how_long, (str(-move) + "a"))
        print("Invalid input! Adding additional elements to the board")
    elif main_string[index_one] == main_string[index_two]:
        print(f"Congrats! You have found matching elements - {main_string[index_one]}!")
        remove_from_list = main_string[index_one]
        main_string.remove(remove_from_list)
        main_string.remove(remove_from_list)
    else:
        print("Try again!")
    if len(main_string) == 0:
        winner = True
        break

    command = input()

if winner:
    print(f"You have won in {move} turns!")
else:
    print("Sorry you lose :(")
    print(*main_string, sep=" ")
