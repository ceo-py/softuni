from project.user import User


class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user):
        if author in Library.books_available:
            if book_name in Library.books_available[author]:
                Library.books_available[author].pop(Library.books_available[author].index(book_name))
                if user.username not in Library.rented_books:
                    Library.rented_books[user.username] = {}
                Library.rented_books[user.username][book_name] = days_to_return
                user.books.append(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for name in Library.rented_books:
            for book, days_return in Library.rented_books[name].items():
                if book == book_name:
                    return f'The book "{book_name}" is already rented and will be available in {days_return} days!'

    def return_book(self, author: str, book_name: str, user):
        if book_name in user.books:
            user.books.pop(user.books.index(book_name))
            Library.books_available[author].append(book_name)
            del Library.rented_books[user.username][book_name]
        return f"{user.username} doesn't have this book in his/her records!"
