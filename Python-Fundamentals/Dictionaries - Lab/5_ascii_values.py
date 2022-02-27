list_of_characters = input().split(", ")

letter_dic = {}

for letter in list_of_characters:
    letter_dic[letter] = ord(letter)

print(letter_dic)
