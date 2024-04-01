username = input()


def Letters(case: str, text: str) -> tuple:
    text = text.upper() if case == 'Upper' else text.lower()
    return text, text


def Reverse(start_index: int, end_index: int, text: str):
    end_index += 1
    if start_index < 0 or end_index > len(text):
        return text, None
    return text, text[start_index:end_index][::-1]


def Substring(substring: str, text: str) -> tuple:
    substring = str(substring)
    if substring not in text:
        return text, f"The username {text} doesn't contain {substring}."
    text = text.replace(substring, '')
    return text, text


def Replace(char: str, text: str) -> tuple:
    text = text.replace(str(char), '-')
    return text, text


def IsValid(char: str, text: str) -> tuple:
    if str(char) not in text:
        return text, f"{char} must be contained in your username."
    return text, f"Valid username."


commands = {
    'Letters': Letters,
    'Reverse': Reverse,
    'Substring': Substring,
    'Replace': Replace,
    'IsValid': IsValid,
}

command_input = input()

while command_input != 'Registration':
    command, *params = [int(x) if x.isdigit()
                        else x for x in command_input.split()]

    username, result_to_print = commands[command](*params, username)
    if result_to_print:
        print(result_to_print)

    command_input = input()
