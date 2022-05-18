string_input = input()

while string_input != "end":
    find_part_index = ""
    find_ = False
    for n in range(1, (len(string_input) // 2) + 1):
        if string_input[:n] == string_input[-n:]:
            find_part_index = n
            find_ = True
    if find_:
        result_ = string_input[:find_part_index]
        string_input = string_input[find_part_index:-find_part_index]
        show_ = string_input + result_ + string_input
        if len(show_) > 2:
            print(show_)

    string_input = input()
