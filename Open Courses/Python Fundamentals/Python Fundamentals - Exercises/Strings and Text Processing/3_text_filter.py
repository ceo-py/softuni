ban_list = input().split()
main_string = input()
for word in ban_list:
    if word in main_string:
        main_string = main_string.replace(word, f"{len(word) * '*'}")
print(main_string)
