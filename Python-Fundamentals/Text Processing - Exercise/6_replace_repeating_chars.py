main_string = input()


for pos, letter in enumerate(range(len(main_string) - 1), 1):
    if main_string[letter] != main_string[pos]:
        print(main_string[letter], end="")

print(main_string[-1])
