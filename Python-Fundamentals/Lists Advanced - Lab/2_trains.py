train_wagons = int(input())
train = [0] * train_wagons
command = input()


def add_people(people):
    train[-1] += people

def insert_people(wagon, number_people):
    train[wagon] += number_people

def leave_people(wagon, number_people):
    train[wagon] -= number_people


commands = {
    "add": add_people,
    "insert": insert_people,
    "leave": leave_people
}

while command != "End":
    command, *info = [int(x) if x.isdigit() else x for x in command.split()]
    commands[command](*info)
    command = input()

print(train)



#
#
#
# train_wagons = int(input())
# train = list()
# command = input()
#
# for n in range(train_wagons):
#     train.append(0)
#
#
# def add_people(people):
#     train[-1] = train[-1] + people
#
#
# def insert_people(wagon, number_people):
#     train[wagon] = train[wagon] + number_people
#
#
# def leave_people(wagon, number_people):
#     train[wagon] = train[wagon] - number_people
#
#
# while command != "End":
#
#     command = command.split()
#
#     if "add" in command:
#         add_people(int(command[-1]))
#
#     elif "insert" in command:
#         insert_people((int(command[1])), int(command[-1]))
#
#     elif "leave" in command:
#         leave_people(int(command[1]), int(command[-1]))
#
#     command = input()
#
# print(train)
