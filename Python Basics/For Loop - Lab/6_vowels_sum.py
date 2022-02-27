text_input = input()

letters = {
    "a": 1,
    "e": 2,
    "i": 3,
    "o": 4,
    "u": 5
}
summary = 0
letter_check = ("a", "e", "i", "o" ,"u")
for letter in text_input:
    if letter in letter_check:
        summary += letters[letter]
print(summary)