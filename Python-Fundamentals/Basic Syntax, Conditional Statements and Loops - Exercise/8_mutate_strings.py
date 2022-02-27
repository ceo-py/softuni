first_text = input()
second_text = input()

list_one = list(first_text)
list_two = list(second_text)
i = 0
target_list = list(first_text)

for letter_a, letter_b in zip(list_one, list_two):
    if letter_a != letter_b:
        target_list[i] = letter_b
        for _ in target_list:
            print(f"{_}", end="")
        print()
    i += 1
