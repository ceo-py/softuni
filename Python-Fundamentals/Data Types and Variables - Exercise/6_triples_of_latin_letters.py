import string

number = int(input())

lower_letters = string.ascii_lowercase

for letter_one in range(number):
    letter_one = lower_letters[letter_one]

    for letter_two in range(number):
        letter_two = lower_letters[letter_two]

        for letter_three in range(number):
            letter_three = lower_letters[letter_three]

            print(f"{letter_one}{letter_two}{letter_three}")
