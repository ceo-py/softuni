import string

all_letters = string.ascii_lowercase

letter_a = input()
letter_b = input()
letter_c = input()

starting_point_loop = all_letters.index(letter_a)
ending_point_loop = all_letters.index(letter_b)
combinations_of_letters = all_letters[starting_point_loop:ending_point_loop + 1]
combinations_of_letters = combinations_of_letters.replace(letter_c, "")
combinations = 0
for first_letter in combinations_of_letters:
    for second_letter in combinations_of_letters:
        for third_letter in combinations_of_letters:
            combinations += 1
            print(f"{first_letter}{second_letter}{third_letter}", end=" ")
print(combinations)
