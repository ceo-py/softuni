import re

main_string = input()

pattern = re.compile(r"([@#])(?P<word>[A-Za-z]{3,})\1\1(?P<word2>[A-Za-z]{3,})\1")

list_result = []
result = list(re.finditer(pattern, main_string))

for show in result:
    if show["word"] == show["word2"][::-1]:
        list_result.append(f"{show['word']} <=> {show['word2']}")

if result:
    print(f"{len(result)} word pairs found!")
    if list_result:
        print("The mirror words are:")
        print(*list_result, sep=", ")
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")

