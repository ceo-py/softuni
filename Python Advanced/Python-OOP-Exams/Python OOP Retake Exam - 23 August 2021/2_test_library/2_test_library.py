from project.library import Library
from unittest import TestCase, main


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.library = Library("Dark Web")

    def test_successful_initialization(self):
        self.assertEqual("Dark Web", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_unsuccessful_name_setter_raise_error_value_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_successful_add_book_in_dict_new_author(self):
        self.assertEqual({}, self.library.books_by_authors)
        self.library.add_book("Joro", "Joro World")

        self.assertEqual({"Joro": ["Joro World"]}, self.library.books_by_authors)

        self.library.add_book("Joro1", "Joro World")

        self.assertEqual({"Joro": ["Joro World"], "Joro1": ["Joro World"]}, self.library.books_by_authors)

    def test_successful_add_book_in_dict_new_title(self):
        self.assertEqual({}, self.library.books_by_authors)
        self.library.add_book("Joro", "Joro World")
        self.assertEqual({"Joro": ["Joro World"]}, self.library.books_by_authors)

        self.library.add_book("Joro", "Joro World 2")
        self.assertEqual({"Joro": ["Joro World", "Joro World 2"]}, self.library.books_by_authors)

    def test_unsuccessful_add_reader_return_duplicity_message(self):
        self.library.add_reader("Joro")
        result = self.library.add_reader("Joro")

        self.assertEqual("Joro is already registered in the Dark Web library.", result)
        self.assertTrue("Joro" in self.library.readers)

    def test_successful_add_reader_in_dict(self):
        self.library.add_reader("Joro")
        self.assertEqual({"Joro": []}, self.library.readers)

        self.library.add_reader("Not Joro")
        self.assertEqual({"Joro": [], "Not Joro": []}, self.library.readers)

    def test_unsuccessful_rent_book_reader_name_not_in_readers(self):
        self.library.add_reader("Joro")
        result = self.library.rent_book("Not Joro", "Joro", "Joro World")

        self.assertEqual("Not Joro is not registered in the Dark Web Library.", result)
        self.assertEqual({"Joro": []}, self.library.readers)

    def test_unsuccessful_rent_book_author_not_in_authors(self):
        self.library.add_reader("Joro")
        self.library.add_book("Joro", "Joro World")
        result = self.library.rent_book("Joro", "Not Joro", "Joro World")

        self.assertEqual(f"Dark Web Library does not have any Not Joro's books.", result)
        self.assertEqual({"Joro": ["Joro World"]}, self.library.books_by_authors)

    def test_unsuccessful_rent_book_book_title_not_in_authors(self):
        self.library.add_reader("Joro")
        self.library.add_book("Joro", "Joro World")
        result = self.library.rent_book("Joro", "Joro", "Joro World 2")

        self.assertEqual("""Dark Web Library does not have Joro's "Joro World 2".""", result)
        self.assertEqual({"Joro": ["Joro World"]}, self.library.books_by_authors)

    def test_successful_rent_book(self):
        self.library.add_reader("Joro")
        self.library.add_book("Not Joro", "Joro World")
        self.library.add_book("Not Joro", "Joro World 2")
        self.library.rent_book("Joro", "Not Joro", "Joro World")

        self.assertEqual([{"Not Joro": "Joro World"}], self.library.readers["Joro"])
        self.assertEqual({"Not Joro": ["Joro World 2"]}, self.library.books_by_authors)


if __name__ == "__main__":
    main()
