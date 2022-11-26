from project.bookstore import Bookstore
from unittest import TestCase, main


class TestGunit(TestCase):
    def setUp(self) -> None:
        self.book_store = Bookstore(10)

    def test_init(self):
        self.assertEqual({}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(10, self.book_store.books_limit)
        self.assertEqual(self.book_store.total_sold_books, self.book_store._Bookstore__total_sold_books)
        self.assertEqual(self.books_limit.total_sold_books, self.book_store.__books_limit)
        self.assertEqual(0, self.book_store._Bookstore__total_sold_books)

    def test_setter_books_limit(self):
        with self.assertRaises(ValueError) as error:
            store = Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(error.exception))

    def test_count_the_total_number_of_books(self):
        self.book_store.availability_in_store_by_book_titles = {
            "Time": 3, "Space": 7
        }
        self.assertEqual(10, len(self.book_store))

    def test_receive_book_no_space(self):
        with self.assertRaises(Exception) as error:
            self.book_store.receive_book("Hitler", 100)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_receive_book_have_space(self):
        self.book_store.availability_in_store_by_book_titles ={"Top Gun": 3}
        result = self.book_store.receive_book("Maveric", 5)
        self.assertEqual("5 copies of Maveric are available in the bookstore.", result)
        self.assertEqual(2, len(self.book_store.availability_in_store_by_book_titles))

        result = self.book_store.receive_book("Maveric", 1)
        self.assertEqual("6 copies of Maveric are available in the bookstore.", result)
        self.assertEqual(2, len(self.book_store.availability_in_store_by_book_titles))

    def test_sell_book_not_available_in_store(self):
        with self.assertRaises(Exception) as error:
            self.book_store.sell_book("Nqma", 1)

        self.assertEqual("Book Nqma doesn't exist!", str(error.exception))

    def test_sell_book_not_enough_copies(self):
        self.book_store.receive_book("Maveric", 5)

        with self.assertRaises(Exception) as error:
            self.book_store.sell_book("Maveric", 6)

        self.assertEqual("Maveric has not enough copies to sell. Left: 5", str(error.exception))

    def test_sell_book(self):
        sold_book = ("Maveric", 5)
        sold_book1 = ("Test", 1)
        self.book_store.receive_book(*sold_book)
        self.book_store.receive_book(*sold_book1)
        self.book_store.receive_book("Test2", 1)

        self.assertEqual("Sold 5 copies of Maveric", self.book_store.sell_book(*sold_book))
        self.assertEqual(5, self.book_store.total_sold_books)
        self.assertEqual("Sold 1 copies of Test", self.book_store.sell_book(*sold_book1))
        self.assertEqual(6, self.book_store.total_sold_books)

    def test_str_output(self):
        sold_book = ("Maveric", 5)
        sold_book1 = ("Test", 1)
        sold_book2 = ("Test1", 4)
        self.book_store.receive_book(*sold_book)
        self.book_store.receive_book(*sold_book1)
        self.book_store.receive_book(*sold_book2)
        self.book_store.sell_book(*sold_book)

        self.assertEqual("Total sold books: 5\n"
                         "Current availability: 5\n"
                         " - Maveric: 0 copies\n"
                         " - Test: 1 copies\n"
                         " - Test1: 4 copies", str(self.book_store))


if __name__ == '__main__':
    main()
