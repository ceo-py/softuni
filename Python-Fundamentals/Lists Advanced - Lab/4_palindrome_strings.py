main_list = input().split(" ")

searched_palindrome = input()

find_words = list()

for word in main_list:
    if word == word[::-1]:
        find_words.append(word)

print(f"{find_words}")
print(f"Found palindrome {find_words.count(searched_palindrome)} times")
