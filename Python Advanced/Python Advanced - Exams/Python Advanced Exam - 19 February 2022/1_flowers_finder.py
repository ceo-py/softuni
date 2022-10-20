from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words = {
"rose": [x for x in "rose"],
"tulip": [x for x in "tulip"],
"lotus": [x for x in "lotus"],
"daffodil": [x for x in "daffodil"]
}
found_word = None

while vowels and consonants and not found_word:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for letter in (vowel, consonant):
        for key, word in words.items():
            while word.count(letter):
                word.remove(letter)
                if not word:
                    found_word = key

if found_word:
    print(f"Word found: {found_word}")
else:
    print(f"Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")





#
#
# from collections import deque
#
# vowels = deque(input().split())
# consonants = deque(input().split())
# words = {
#     "rose": "rose",
#     "tulip": "tulip",
#     "lotus": "lotus",
#     "daffodil": "daffodil"}
# found_word = {"found": False, "word": ""}
#
#
# def remove_letter(letter):
#     for word, w_letters in words.items():
#         try:
#             words[word] = w_letters.replace(letter, "")
#         except TypeError:
#             pass
#         if not words[word]:
#             found_word["found"] = True
#             found_word["word"] = word
#             break
#
#
# def show_left_letters():
#     if vowels:
#         print(f"Vowels left: {' '.join(vowels)}")
#     if consonants:
#         print(f"Consonants left: {' '.join(consonants)}")
#
#
# while vowels and consonants and not found_word["found"]:
#     vowel_letter = vowels.popleft()
#     consonant_letter = consonants.pop()
#     remove_letter(vowel_letter)
#     remove_letter(consonant_letter)
#
# if not found_word["found"]:
#     print("Cannot find any word!")
# else:
#     print(f"Word found: {found_word['word']}")
#
# show_left_letters()




#
#
# from collections import deque
#
# vowels = deque(input().split())
# consonants = deque(input().split())
# words = {
#     "rose": "rose",
#     "tulip": "tulip",
#     "lotus": "lotus",
#     "daffodil": "daffodil"}
# found_word = [False, ""]
#
#
# def remove_letter(letter):
#     for word, w_letters in words.items():
#         try:
#             words[word] = w_letters.replace(letter, "")
#         except TypeError:
#             pass
#         if not words[word]:
#             found_word[0] = True
#             found_word[1] = word
#             break
#
#
# def show_left_letters():
#     if vowels:
#         print(f"Vowels left: {' '.join(vowels)}")
#     if consonants:
#         print(f"Consonants left: {' '.join(consonants)}")
#
#
# while vowels and consonants and not found_word[0]:
#     vowel_letter = vowels.popleft()
#     consonant_letter = consonants.pop()
#     remove_letter(vowel_letter)
#     remove_letter(consonant_letter)
#
# if not found_word[0]:
#     print("Cannot find any word!")
# else:
#     print(f"Word found: {found_word[1]}")
#
# show_left_letters()
