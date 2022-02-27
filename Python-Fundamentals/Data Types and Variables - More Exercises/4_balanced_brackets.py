number = int(input())

open = 0
close = 0
check_for_next_one = False
close_next = 0
for _ in range(number):

    check = input()

    if check == "(":
        open += 1
        check_for_next_one = True

    elif check == ")":
        close += 1
        if check_for_next_one:
            close_next += 1
            check_for_next_one = False

if open == close and close == close_next:
    print("BALANCED")

else:
    print("UNBALANCED")
