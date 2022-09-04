def palindrome(word, idx):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"
    if word[idx] == word[-idx-1]:
        print(word[-idx-1])
        return palindrome(word, idx+1)
    else:
        return f"{word} is not a palindrome"


print(palindrome("peter", 0))
print(palindrome("abcba", 0))


# def palindrome(word, idx):
#     if word == word[::-1]:
#         return f"{word} is a palindrome"
#     return f"{word} is not a palindrome"