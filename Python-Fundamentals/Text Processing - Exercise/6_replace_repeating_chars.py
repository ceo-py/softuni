main_string = input()

o = 1
for letter in range(len(main_string) - 1):
    if main_string[letter] != main_string[o]:
        print(main_string[letter], end="")
    o += 1

print(main_string[-1])
