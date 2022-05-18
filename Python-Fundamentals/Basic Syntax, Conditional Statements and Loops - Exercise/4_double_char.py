string_ = input()

while string_ != "End":
    if string_ != "SoftUni":
        [print(i * 2, end="") for i in string_]
        print()
    string_ = input()
