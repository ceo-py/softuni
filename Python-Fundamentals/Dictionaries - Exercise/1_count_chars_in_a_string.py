characters = input().replace(" ", "")

character_count = {}

for character in characters:

    if character not in character_count:
        character_count[character] = 0
    character_count[character] += 1

for key, value in character_count.items():
    print(f"{key} -> {value}")
