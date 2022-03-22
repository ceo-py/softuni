original_text = input()

skip_letters = ['a', 'o', 'u', 'e', 'i','A', 'O', 'U', 'E', 'I']


def change_text(arg1):
    result = ""
    for letter in arg1:
        if letter not in skip_letters:
            result += letter
    return result


print(change_text(original_text))