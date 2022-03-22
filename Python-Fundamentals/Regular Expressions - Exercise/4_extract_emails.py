import re
input_string = input()
pattern = re.compile(r"(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\.\-_][A-Za-z]+)+))(\b|(?=\s))")
matches = pattern.finditer(input_string)

for show in matches:
    print(show[0])
