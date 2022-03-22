import re

dates_match = input()
# pattern = re.compile(r"(^|(?<=\s)-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s)))")
pattern = re.compile(r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))")
matches = pattern.finditer(dates_match)
for show in matches:
    print(show[0], end=" ")
