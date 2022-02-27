test_string = input().split(", ")

for test in test_string:
    if 3 <= len(test) <= 16:
        all_check = False
        for check in test:
            if check.isdigit() or check.isalpha() or check == "-" or check == "_":
                all_check = True
            else:
                all_check = False
                break
        if all_check:
            print(test)
