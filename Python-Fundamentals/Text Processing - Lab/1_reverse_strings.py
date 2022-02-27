command = input()

while command != "end":
    reverse = command[::-1]
    print(f"{command} = {reverse}")
    command = input()
