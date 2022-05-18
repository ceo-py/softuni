how_many_strings = int(input())

skip_parameters = [",", ".", "_"]

for _ in range(how_many_strings):
    string_ = input()
    for element in skip_parameters:
        if element in string_:
            print(f"{string_} is not pure!")
            break
    else:
        print(f"{string_} is pure.")
