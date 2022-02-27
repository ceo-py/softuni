import string

saved_letter = list()
guess_word = ""
skip_letters = ["c", "o", "n"]
skip_letters_one_time = list()
complete_word = list()
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase

while True:
    letter = input()
    saved_letter.append(letter)
    if letter == "End":
        break
    if letter in skip_letters:
        skip_letters_one_time.append(letter)
    else:
        if letter in lower_letters or letter in upper_letters:
            guess_word += letter
    if "c" in skip_letters_one_time and "o" in skip_letters_one_time and "n" in skip_letters_one_time:
        skip_letters_one_time.clear()
        complete_word.append(guess_word)
        guess_word = " "
    for char in skip_letters_one_time:
        count = skip_letters_one_time.count(letter)
        if count > 1:
            guess_word += letter
            break
for word in complete_word:
    print(word, end="")