egg_starting_number = int(input())

command = input()
sold_eggs = 0

while command != 'Close':
    egg_number = int(input())

    if command == 'Buy':
        egg_starting_number -= egg_number
        sold_eggs += egg_number

        if egg_starting_number < 0:
            print(f'Not enough eggs in store!')
            print(f'You can buy only {egg_starting_number + egg_number}.')
            break

    elif command == 'Fill':
        egg_starting_number += egg_number

    command = input()

else:
    print(f'Store is closed!')
    print(f'{sold_eggs} eggs sold.')







# eggs_in_store = int(input())
#
# total_eggs = eggs_in_store
# total_sold_eggs = 0
#
# while True:
#     action_type = input()
#
#     if action_type == "Close":
#         print(f"Store is closed!\n{total_sold_eggs} eggs sold.")
#         break
#
#     else:
#         number_eggs = int(input())
#
#     if action_type == "Buy":
#         total_eggs = total_eggs - number_eggs
#         total_sold_eggs += number_eggs
#
#     elif action_type == "Fill":
#         total_eggs = total_eggs + number_eggs
#
#     if total_eggs < 0:
#         print(f"Not enough eggs in store!\nYou can buy only {total_eggs + number_eggs}.")
#         break
