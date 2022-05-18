import re

numbers = input()
pattern = re.compile(r"\b(?:0x)?[0-9A-F]+\b")
matches = pattern.finditer(numbers)

for show in matches:
    print(show[0], end=" ")
