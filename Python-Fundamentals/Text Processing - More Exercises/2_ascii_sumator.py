start_char, end_char, random_string = input(), input(), input()

show_result = 0
for character in random_string:
    if ord(start_char) < ord(character) < ord(end_char):
        show_result += ord(character)

print(show_result)
