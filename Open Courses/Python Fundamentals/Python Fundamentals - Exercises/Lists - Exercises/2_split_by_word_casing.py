exclusions = (",", ";", ":", ".", "!", "(", ")", "\"", "'", "\\", "/", "[", "]", " ")

words = input()
for x in exclusions:
    words = words.replace(x, " ")

lower = []
upper = []
mixed = []
for word in words.split():
    if word.islower() and word.isalpha():
        lower.append(word)
    elif word.isupper() and word.isalpha():
        upper.append(word)
    else:
        mixed.append(word)

print(f"Lower-case: " + ', '.join(lower))
print(f"Mixed-case: " + ', '.join(mixed))
print(f"Upper-case: " + ', '.join(upper))
