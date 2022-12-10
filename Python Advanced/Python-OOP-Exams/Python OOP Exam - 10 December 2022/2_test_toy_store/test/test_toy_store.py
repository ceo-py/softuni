from project.toy_store import ToyStore
from unittest import TestCase, main



class TestGUnit(TestCase):

    def setUp(self):
        self.toy = ToyStore()

    def test_init(self):
        self.assertEqual(self.toy.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_shelf_dont_exist_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("Z", "Car")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")
        self.assertFalse("Z" in self.toy.toy_shelf)

    def test_add_toy_raise_exception_toy_on_shelf(self):
        self.toy.add_toy("A", "Car")

        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", "Car")

        self.assertEqual(str(ex.exception), "Toy is already in shelf!")
        self.assertEqual(self.toy.toy_shelf["A"], "Car")

    def test_add_toy_raise_exception_shelf_already_taken(self):
        self.toy.add_toy("A", "Car")

        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", "Trabant")

        self.assertEqual(str(ex.exception), "Shelf is already taken!")
        self.assertTrue(self.toy.toy_shelf["A"] is not None)

    def test_add_toy_successfully(self):
        result = self.toy.add_toy("A", "Car")

        self.assertEqual(result, "Toy:Car placed successfully!")
        self.assertEqual(self.toy.toy_shelf["A"], "Car")

        result = self.toy.add_toy("B", "Keyboard")

        self.assertEqual(result, "Toy:Keyboard placed successfully!")
        self.assertEqual(self.toy.toy_shelf["B"], "Keyboard")

    def test_remove_toy_raise_exception_dont_exist(self):
        self.toy.add_toy("A", "Car")

        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy("Z", "Keyboard")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")
        self.assertTrue("Z" not in self.toy.toy_shelf)

    def test_remove_toy_raise_exception_toy_dont_exists(self):
        self.toy.add_toy("A", "Car")

        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy("A", "Keyboard")

        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")
        self.assertTrue("Keyboard" not in self.toy.toy_shelf["A"])

    def test_remove_toy_successfully(self):
        self.toy.add_toy("A", "Car")
        self.toy.add_toy("D", "100/100")

        result = self.toy.remove_toy("A", "Car")
        self.assertEqual(result, "Remove toy:Car successfully!")
        self.assertEqual(self.toy.toy_shelf["A"], None)

        self.toy.add_toy("B", "Keyboard")
        result = self.toy.remove_toy("B", "Keyboard")
        self.assertEqual(result, "Remove toy:Keyboard successfully!")
        self.assertEqual(self.toy.toy_shelf["B"], None)


if __name__ == "__main":
    main()