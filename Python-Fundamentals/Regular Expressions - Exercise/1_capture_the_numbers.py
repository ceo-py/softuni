import re

pattern = re.compile(r"\d+")
while True:
    input_string = input()
    if input_string:
        matches = pattern.finditer(input_string)

        for show in matches:
            print(show[0], end=" ")
    else:
        break
