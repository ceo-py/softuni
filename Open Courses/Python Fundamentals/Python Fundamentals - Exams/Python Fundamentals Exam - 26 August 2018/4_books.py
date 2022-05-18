# import re
book = input()
book_store = {}
sold_books = []

while book != "on work":
    test = book.split()
    title_book, author_book, price_book, *_ = book.split()
    # if price_book.isdigit() or re.search("[-]?\d+\.\d+(?:[eE][-]?\d+)?$", price_book) is not None:
    try:
        if float(price_book) > 0:
            trash = book.split(" -> ")
            book_store[title_book] = {}
            book_store[title_book]['author'] = author_book
            book_store[title_book]['price'] = float(price_book)
            book_store[title_book]['chapters'] = trash[1].split(",")
    except ValueError:
        pass
    book = input()

looking_for_book = input()
while looking_for_book != "end work":
    if looking_for_book not in book_store:
        print("No such book here")
    else:
        sold_books.append(looking_for_book)
    looking_for_book = input()

if sold_books:
    total_sum = 0
    for name in sold_books:
        print(f"SOLD: {name} with author {book_store[name]['author']}."
              f" Chapters in the book {len(book_store[name]['chapters'])}")
        total_sum += book_store[name]['price']
    print(f"Money: {total_sum:.2f}")
else:
    print("Bad day :(")
