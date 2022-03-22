import re

main_string = input()
pattern = re.compile(r"\b_([a-zA-Z0-9]+)\b")
matches = pattern.finditer(main_string)
show_result = []
for show in matches:
    show_result.append(show[1])

print(",".join(show_result))