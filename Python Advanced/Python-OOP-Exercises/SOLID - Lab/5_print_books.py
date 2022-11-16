class Book:
    def __init__(self, content):
        self.content = content


class Formatter:
    def format(self, book):
        return book.content


class Printer:
    def get_book(self, book, formatter):
        return formatter.format(book)


b = Book("book")
f = Formatter()
p = Printer()

print(p.get_book(b, f))
