main_text = input()
result = ""
for letter in main_text:
    cripted_letter = ord(letter)
    result += chr(cripted_letter + 3)

print(result)
