pyramid_number = int(input())


current = 1
is_current_bigger_than_input_number = False

for row in range(1, pyramid_number + 1):
    for col in range(1, row + 1):
        if current > pyramid_number:
            is_current_bigger_than_input_number = True
            break
        print(str(current) + " ", end="")
        current += 1
    if is_current_bigger_than_input_number:
        break
    print("")
