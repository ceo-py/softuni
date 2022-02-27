ban_list = input().split(", ")
text = input()

replace_symbol = "*"

for ban_word in ban_list:
    word_len = len(ban_word)
    text = text.replace(ban_word, f"{word_len * replace_symbol}")
print(text)
