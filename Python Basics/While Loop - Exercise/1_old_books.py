book_to_check = input()

book_added_to_liberry = list()
book_check_count = 0

while True:
    book_added_to_liberry.append(input())
    if "No More Books" in book_added_to_liberry:
        print(f"The book you search is not here!\nYou checked {book_check_count} books.")
        break
    if book_to_check in book_added_to_liberry:
        print(f"You checked {book_check_count} books and found it.")
        break
    book_check_count += 1



# book = input()
#
# count = 0
# input_line = input()
# flag = False
#
# while input_line != 'No More Books':
#     if input_line == book:
#         flag = True
#         break
#     count += 1
#     input_line = input()
#
# if flag == True:
#     print(f'You checked {count} books and found it.')
# else:
#     print('The book you search is not here!')
#     print(f'You checked {count} books.')
