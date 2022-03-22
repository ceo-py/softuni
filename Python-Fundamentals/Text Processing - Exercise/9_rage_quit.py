main_string = input()

current_result, result_show, number = "", "", "",

for index, symbols in enumerate(main_string):
    if not symbols.isdigit():
        current_result += symbols
    elif symbols.isdigit():
        number += symbols
        if index + 1 < len(main_string):
            if main_string[index + 1].isdigit():
                continue
        result_show += int(number) * current_result
        current_result, number = "", ""

result_show = result_show.upper()
print(f"Unique symbols used: {len(set(result_show))}")
print(result_show)
