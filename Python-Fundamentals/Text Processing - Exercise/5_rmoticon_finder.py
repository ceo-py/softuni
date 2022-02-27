main_text = input().split()

for letter in main_text:
    if ":" in letter:
        if len(letter) > 1:
            print(letter[0] + letter[1]+ letter[2])
        else:
            print(letter[0] + letter[1])