initial_string = input()
input_command = input()


def left(x, times):
    for r in range(times):
        x = x[1:] + x[0]
    return x


def right(x, times):
    for r in range(times):
        x = x[-1] + x[:-1]
    return x


def insert(x, index, item):
    return x[:index] + item + x[index:]


def delete(x, start_index, end_index):
    return x[:start_index] + x[end_index + 1:]


commands = {
    'Left': left,
    'Right': right,
    'Insert': insert,
    'Delete': delete
}
while input_command != 'end':
    command, *data = [int(x) if x[0].isdigit() else x for x in input_command.split()]
    initial_string = commands[command](initial_string, *data)

    input_command = input()

print(initial_string)
