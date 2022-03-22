import re
main_string = input().lower()
find_string = input().lower()
pattern = re.compile(r"\b"+find_string+r"\b")
matches = pattern.finditer(main_string)
show_result = 0
for show in matches:
    show_result += 1

print(show_result)


