import re
pattern = re.compile(r"\bwww\.[a-zA-Z0-9-]+\.[a-z]+(\.[a-z]+)*\b")
while True:
    main_string = input()
    if main_string:
        matches = pattern.finditer(main_string)
        for show in matches:
            print(show[0])
    else:
        break
