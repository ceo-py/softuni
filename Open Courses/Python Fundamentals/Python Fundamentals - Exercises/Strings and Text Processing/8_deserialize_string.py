letters_input = input()

added_letter = []
result = []

while letters_input != "end":
    added_letter.append(letters_input)
    for n in letters_input[2:].split("/"):
        result.append(n)
    letters_input = input()

for info in added_letter:
    letter, pos = info.split(":")
    index_letters = pos.split("/")
    for ind in index_letters:
        result[int(ind)] = letter

print("".join(result))
