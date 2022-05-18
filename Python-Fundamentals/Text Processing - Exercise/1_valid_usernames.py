test_string = input().split(", ")

for test in test_string:
    if 3 <= len(test) <= 16:
        for check in test:
            if not any([check.isdigit(), check.isalpha(), check == "-", check == "_"]):
                break
        else:
            print(test)
