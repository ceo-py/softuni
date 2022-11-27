from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Road Down", 2)

    def test_successful_initialization(self):
        self.assertEqual("Road Down", self.paint_factory.name)
        self.assertEqual(2, self.paint_factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual({}, self.paint_factory.products)

    def test_unsuccessful_add_ingredient_raise_value_error_no_space(self):
        self.paint_factory.capacity = 0

        with self.assertRaises(ValueError) as ve:
            self.paint_factory.add_ingredient("blue", 1)

        self.assertEqual("Not enough space in factory", str(ve.exception))

    def test_unsuccessful_add_ingredient_raise_value_error_wrong_type(self):
        with self.assertRaises(TypeError) as te:
            self.paint_factory.add_ingredient("purple", 1)

        self.assertEqual("Ingredient of type purple not allowed in PaintFactory", str(te.exception))

    def test_successful_add_ingredient_to_dict(self):
        self.paint_factory.add_ingredient("blue", 1)
        self.assertEqual({"blue": 1}, self.paint_factory.ingredients)

        self.paint_factory.add_ingredient("green", 1)
        self.assertEqual({"blue": 1, "green": 1}, self.paint_factory.ingredients)
        self.assertEqual(2, self.paint_factory.capacity)

    def test_unsuccessful_remove_ingredient_from_dict_raise_key_error_no_ingredient(self):
        with self.assertRaises(KeyError) as ke:
            self.paint_factory.remove_ingredient("purple", 1)

        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))

    def test_unsuccessful_remove_ingredient_from_dict_raise_value_error_ingredient_less_that_zero(self):
        self.paint_factory.add_ingredient("green", 1)

        with self.assertRaises(ValueError) as ve:
            self.paint_factory.remove_ingredient("green", 2)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))

    def test_successful_remove_ingredient_from_dict(self):
        self.paint_factory.add_ingredient("green", 2)
        self.paint_factory.remove_ingredient("green", 1)
        self.assertEqual({"green": 1}, self.paint_factory.ingredients)

        self.paint_factory.remove_ingredient("green", 1)
        self.assertEqual({"green": 0}, self.paint_factory.ingredients)


if __name__ == "__main__":
    main()
