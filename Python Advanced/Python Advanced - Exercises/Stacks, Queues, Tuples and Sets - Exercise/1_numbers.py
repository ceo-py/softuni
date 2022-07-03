set_one = set(int(x) for x in input().split())
set_two = set(int(x) for x in input().split())

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input()

    if "Check Subset" not in command:
        numbers = [int(x) for x in command.split() if x.isdigit()]

        if "First" in command:
            if "Add" in command:
                for num in numbers:
                    set_one.add(num)

            elif "Remove" in command:
                for num in numbers:
                    set_one.discard(num)

        elif "Second" in command:
            if "Add" in command:
                for num in numbers:
                    set_two.add(num)

            elif "Remove" in command:
                for num in numbers:
                    set_two.discard(num)

    else:
        print(set_one.issuperset(set_two))

print(*sorted(set_one), sep=", ")
print(*sorted(set_two), sep=", ")
