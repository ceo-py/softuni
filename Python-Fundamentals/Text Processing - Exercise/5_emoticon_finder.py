main_text = input()

for index, letter in enumerate(main_text):
    if ":" == letter:
        print(f"{letter}{main_text[index+1]}")