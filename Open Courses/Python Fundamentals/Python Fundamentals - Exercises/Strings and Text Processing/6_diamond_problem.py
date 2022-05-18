import re

main_string = input()
pattern = re.compile(r"<[a-zA-z0-9]+>")
matches = pattern.findall(main_string)
find_match = False
for show in matches:
    total = 0
    for n in show:
        if n.isdigit():
            total += int(n)
            if not find_match:
                find_match = True
    print(f"Found {total} carat diamond")

if not find_match:
    print("Better luck next time")