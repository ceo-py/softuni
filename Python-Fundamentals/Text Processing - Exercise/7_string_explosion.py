main_string = input().split(">")

show_result = ""
what_left = 0
for letter in main_string:
    if len(letter) > 1 and any(map(str.isdigit, letter)):
        what_left += (int(letter[0]) - 1)
        if what_left >= len(letter):
            show_result += ">"
        else:
            show_result += ">" + letter[1 + what_left:]
            what_left = 0
    elif len(letter) == 1 and letter.isdigit():
        if int(letter) > 1:
            what_left += (int(letter) - 1)
        show_result += ">"
    else:
        show_result += letter

print(show_result)
