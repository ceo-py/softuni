number_words = int(input())

words_synonyms = {}

for _ in range(number_words):
    word = input()
    synonym = input()
    words_synonyms[word] = words_synonyms.get(word, []) + [synonym]

for word in words_synonyms:
    print(f'{word} - {", ".join(words_synonyms[word])}')








# number_words = int(input())
#
#
# synonyms = {}
# for _ in range(number_words):
#     word_one = input()
#     word_two = input()
#     if word_one not in synonyms:
#         synonyms[word_one] = list()
#         synonyms[word_one].append(word_two)
#     else:
#         synonyms[word_one].append(word_two)
#
# for key, value in synonyms.items():
#     print(f"{key} - ", end="")
#     print(*value, sep=", ")
#
#
# # for word in synonyms:
# #     print(f"{word} - {', '. join(synonyms[word])}")