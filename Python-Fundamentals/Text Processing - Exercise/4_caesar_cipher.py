main_text = input()
main_string = ""
for letter in main_text:
    cripted_letter = ord(letter)
    main_string += chr(cripted_letter + 3)

print(main_string)
