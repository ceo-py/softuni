elements = input().split()
indexes = input()
number_of_moves = 0
while indexes != "end":
    first_index, second_index = [int(x) for x in indexes.split()]
    len_elements = len(elements)
    number_of_moves += 1

    if first_index == second_index or not 0 <= first_index < len_elements or not 0 <= second_index < len_elements:
        cut_in_half = int(len_elements/2)
        element_to_insert = f"-{number_of_moves}a"
        elements = elements[:cut_in_half] + [element_to_insert, element_to_insert] + elements[cut_in_half:]

        # elements.insert(cut_in_half, element_to_insert)
        # elements.insert(cut_in_half, element_to_insert)


        # for x in range(2):
        #     elements.insert(cut_in_half, element_to_insert)

        print("Invalid input! Adding additional elements to the board")

    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        del elements[first_index]
        if first_index < second_index:
            second_index -= 1
        del elements[second_index]

    else:
        print("Try again!")

    if not elements:
        break

    indexes = input()


if elements:
    print("Sorry you lose :(\n", *elements)

else:
    print(f"You have won in {number_of_moves} turns!")









#
# main_string = [n for n in input().split()]
# command = input()
# move = 0
# winner = False
# while command != "end":
#     command = command.split()
#     index_one = int(command[0])
#     index_two = int(command[-1])
#     move += 1
#     if index_two == index_one or index_two < 0 or index_one < 0 \
#             or len(main_string) - 1 < index_one or len(main_string) - 1 < index_two:
#         how_long = int(len(main_string) / 2)
#         main_string.insert(how_long, (str(-move) + "a"))
#         main_string.insert(how_long, (str(-move) + "a"))
#         print("Invalid input! Adding additional elements to the board")
#     elif main_string[index_one] == main_string[index_two]:
#         print(f"Congrats! You have found matching elements - {main_string[index_one]}!")
#         remove_from_list = main_string[index_one]
#         main_string.remove(remove_from_list)
#         main_string.remove(remove_from_list)
#     else:
#         print("Try again!")
#     if len(main_string) == 0:
#         winner = True
#         break
#
#     command = input()
#
# if winner:
#     print(f"You have won in {move} turns!")
# else:
#     print("Sorry you lose :(")
#     print(*main_string, sep=" ")
