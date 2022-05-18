import re

phone_number = input()
pattern = re.compile(r"((^\+|\s\+)359-2-\d{3}-\b\d{4}\b|(^\+|\s\+)359\s2\s\d{3}\s\b\d{4}\b)")
matches = pattern.finditer(phone_number)
show_result = []
for show in matches:
    show_result.append(show[0])

print("".join(show_result))