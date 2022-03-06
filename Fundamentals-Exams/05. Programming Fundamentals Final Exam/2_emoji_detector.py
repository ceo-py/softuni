import re

main_string = input()

find_numbers = ""

for num in main_string:
    if num.isdigit():
        find_numbers += num
total_sum_numbers = 1
for num in find_numbers:
    total_sum_numbers *= int(num)

patterns = re.compile(r"\:{2}([A-Z]{1}[a-z]{2,})\:{2}|\*{2}([A-Z]{1}[a-z]{2,})\*{2}")
find_emoji = re.finditer(patterns, main_string)
resul_to_print = []
for find_number, show in enumerate(find_emoji):
    asci_value = 0
    if show[1] is None:
        for letter in show[2]:
            asci_value += ord(letter)
    else:
        for letter in show[1]:
            asci_value += ord(letter)
    if asci_value > total_sum_numbers:
        resul_to_print.append(show[0])

print(f"Cool threshold: {total_sum_numbers}")
print(f"{find_number + 1} emojis found in the text. The cool ones are:")
print(*resul_to_print, sep="\n")
