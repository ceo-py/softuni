import re

dates_match = input()
pattern = re.compile(r"([2-9]|[JQKA]|10)[SHDC]")
matches = pattern.finditer(dates_match)
for show in matches:
    print(show[0], end=" ")
