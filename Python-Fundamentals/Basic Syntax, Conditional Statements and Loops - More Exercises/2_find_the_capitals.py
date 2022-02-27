import string

text = input()

capital_letter = string.ascii_uppercase
letter_position = list()
position = 0

for letter in text:
    if letter in capital_letter:
        letter_position.append(position)
    position += 1

print(letter_position)
