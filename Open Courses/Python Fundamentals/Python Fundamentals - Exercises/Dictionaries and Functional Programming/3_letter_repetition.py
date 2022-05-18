main_string = input()

repetition_letter = {x:main_string.count(x) for x in main_string}
[print(f"{key} -> {value}") for key, value in repetition_letter.items()]



# main_string = input()
#
#
# repetition_letter = {}
# for letter in main_string:
#     if letter not in repetition_letter:
#         repetition_letter[letter] = main_string.count(letter)
#
# for key, value in repetition_letter.items():
#     print(f"{key} -> {value}")