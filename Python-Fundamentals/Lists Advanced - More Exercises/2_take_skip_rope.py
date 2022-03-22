main_string = input()

numbers = list()
letter = ""
take_list = list()
skip_list = list()

result = ""

for character in main_string:
    if character.isdigit():
        numbers.append(int(character))
    else:
        letter += character

for ind, num in enumerate(numbers):
    if ind % 2 == 0:
        take_list.append(num)
    else:
        skip_list.append(num)

for i, n in zip(take_list, skip_list):
    if i == 0:
        letter = letter[n:]
    elif i != 0:
        result = result + letter[:i]
        letter = letter[n + i:]

print(result)
