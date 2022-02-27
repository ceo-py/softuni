main_string = input()
text_to_show = ""
for symbol in main_string[:]:
    if symbol.isdigit():
        to_show = main_string[:main_string.index(symbol)]
        main_string = main_string.replace(to_show + symbol, "")
        text_to_show += (str(to_show.upper()) * int(symbol))

count = set(text_to_show)

print(f"Unique symbols used: {len(count)}")
print(text_to_show)


