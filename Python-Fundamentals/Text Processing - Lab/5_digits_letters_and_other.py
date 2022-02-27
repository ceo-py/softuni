main_text = input()

digits = ""
letters = ""
everything_other = ""
for number in main_text:
    if number.isdigit():
        digits += number
    elif number.isalpha():
        letters += number
    else:
        everything_other += number

print(digits)
print(letters)
print(everything_other)
