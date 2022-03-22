text = input()

letter_position = [position for position, letter in enumerate(text) if letter.isupper()]
print(letter_position)



# text = input()
#
# letter_position = list()
#
# for position, letter in enumerate(text):
#     if letter.isupper():
#         letter_position.append(position)
#
# print(letter_position)




# import string
#
# text = input()
#
# capital_letter = string.ascii_uppercase
# letter_position = list()
# position = 0
#
# for letter in text:
#     if letter in capital_letter:
#         letter_position.append(position)
#     position += 1
#
# print(letter_position)
