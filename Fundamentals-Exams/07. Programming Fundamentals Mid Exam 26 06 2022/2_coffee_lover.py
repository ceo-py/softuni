names_of_the_coffees = input().split()
number_of_commands = int(input())


def correct_index(index):
    if 0 <= index < len(names_of_the_coffees):
        return True


def include_coffee(coffee):
    names_of_the_coffees.append(coffee)


def remove_coffee(first_or_last, number_of_coffees):
    global names_of_the_coffees
    if 0 <= number_of_coffees < len(names_of_the_coffees):
        if "first" in first_or_last:
            #names_of_the_coffees = names_of_the_coffees[first_or_last:]
            for coffee_to_remove in range(number_of_coffees):
                del names_of_the_coffees[0]
        elif "last" in first_or_last:
            #names_of_the_coffees = names_of_the_coffees[:-first_or_last]
            for coffee_to_remove in range(number_of_coffees):
                del names_of_the_coffees[-1]


def prefer_coffee(coffee_ind_one, coffee_ind_two):
    if correct_index(coffee_ind_one) and correct_index(coffee_ind_two):
        names_of_the_coffees[coffee_ind_one], names_of_the_coffees[coffee_ind_two] = \
            names_of_the_coffees[coffee_ind_two], names_of_the_coffees[coffee_ind_one]


def reverse_coffee():
    global names_of_the_coffees
    names_of_the_coffees = names_of_the_coffees[::-1]


for command in range(number_of_commands):
    command_input = input().split()
    if "Include" in command_input:
        include_coffee(command_input[-1])
    elif "Reverse" in command_input:
        reverse_coffee()
    else:
        command_type, index_one, index_two = [int(x) if x.isdigit() else x for x in command_input]
        if "Remove" in command_type:
            remove_coffee(index_one, index_two)
        else:
            prefer_coffee(index_one, index_two)

print(f"Coffees:\n{' '.join(names_of_the_coffees)}")
