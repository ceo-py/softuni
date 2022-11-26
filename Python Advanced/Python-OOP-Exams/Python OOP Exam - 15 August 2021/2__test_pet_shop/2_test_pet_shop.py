from project.pet_shop import PetShop
from unittest import TestCase, main


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.pet_shop = PetShop("Koti")

    def test_successful_initialization(self):
        self.assertEqual("Koti", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_unsuccessful_add_food_raise_value_error_quantity_less_or_equal_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("Bones", 0)

        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))

    def test_successful_add_food_quantity_and_name_in_dict(self):
        self.pet_shop.add_food("Meat", 6)
        result = self.pet_shop.add_food("Bones", 4)

        self.assertEqual(f"Successfully added 4.00 grams of Bones.", result)
        self.assertEqual(4, self.pet_shop.food["Bones"])
        self.assertEqual({"Meat": 6, "Bones": 4}, self.pet_shop.food)

    def test_unsuccessful_add_pet_raise_exception_duplicity_pet_name(self):
        self.pet_shop.add_pet("Joro")
        self.pet_shop.add_pet("Not Joro")

        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Joro")

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(["Joro", "Not Joro"], self.pet_shop.pets)

    def test_successful_add_pet_raise_exception_duplicity_pet_name(self):
        self.pet_shop.add_pet("Joro")
        result = self.pet_shop.add_pet("Not Joro")

        self.assertEqual("Successfully added Not Joro.", result)
        self.assertEqual(["Joro", "Not Joro"], self.pet_shop.pets)

    def test_unsuccessful_feed_pet_raise_exception_pet_name_not_found(self):
        self.pet_shop.add_pet("Joro")

        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Bones", "Not Joro")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_unsuccessful_feed_pet_return_food_name_not_found(self):
        self.pet_shop.add_pet("Joro")
        self.pet_shop.add_food("Meat", 6)

        result = self.pet_shop.feed_pet("Bones", "Joro")
        self.assertEqual('You do not have Bones', result)

    def test_unsuccessful_feed_pet_return_adding_food(self):
        self.pet_shop.add_pet("Joro")
        self.pet_shop.add_food("Meat", 6)

        result = self.pet_shop.feed_pet("Meat", "Joro")
        self.assertEqual("Adding food...", result)
        self.assertEqual(1006.00, self.pet_shop.food["Meat"])

    def test_successful_feed_pet_return_string(self):
        self.pet_shop.add_pet("Joro")
        self.pet_shop.add_food("Meat", 666)

        result = self.pet_shop.feed_pet("Meat", "Joro")
        self.assertEqual("Joro was successfully fed", result)
        self.assertEqual(566, self.pet_shop.food["Meat"])

    def test__str__(self):
        self.pet_shop.add_pet("Joro")
        self.pet_shop.add_pet("Not Joro")
        self.pet_shop.add_food("Meat", 666)

        self.assertEqual("Shop Koti:\n"
                         "Pets: Joro, Not Joro", self.pet_shop.__repr__())


if __name__ == "__main__":
    main()
