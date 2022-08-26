act_key = input()
command = input()


def contains(substring, act_key):
    if substring in act_key:
        return (f"{act_key} contains {substring}")
    else:
        return f"Substring not found!"


def flip(upper_lower, start_index, end_index, act_key):
    if upper_lower == "Upper":
        result = act_key[:start_index] + act_key.upper()[start_index:end_index] + act_key[end_index:]


    elif upper_lower == "Lower":
        result = act_key[:start_index] + act_key.lower()[start_index:end_index] + act_key[end_index:]

    return result


def slice(start_index, end_index, act_key):
    return act_key[:start_index] + act_key[end_index:]


while command != "Generate":
    command_type, *info = [int(x) if x[-1].isdigit() else x for x in command.split(">>>")]
    if command_type == "Contains":
        substring = info[0]
        print(contains(substring, act_key))


    elif command_type == "Flip":
        upper_lower = info[0]
        start_index = info[1]
        end_index = info[2]
        act_key = flip(upper_lower, start_index, end_index, act_key)
        print(act_key)


    elif command_type == "Slice":
        start_index = info[0]
        end_index = info[1]
        act_key = slice(start_index, end_index, act_key)
        print(act_key)

    command = input()

print(f"Your activation key is: {act_key}")