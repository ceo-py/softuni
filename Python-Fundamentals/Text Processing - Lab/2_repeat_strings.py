string_input = input().split()

for letters in string_input:
    repeated = len(letters)
    print(f"{repeated * letters}", end="")
