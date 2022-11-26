from unittest import TestCase, main
from project.train.train import Train


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.train = Train("Arrow", 2)

    def test_successful_initialization(self):
        self.assertEqual("Arrow", self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertEqual([], self.train.passengers)
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_unsuccessful_add_raise_value_error_capacity(self):
        self.train.add("Joro")
        self.train.add("Not Joro")
        with self.assertRaises(ValueError) as ve:
            self.train.add("Georgi")

        self.assertEqual("Train is full", str(ve.exception))
        self.assertEqual(2, self.train.capacity)

    def test_unsuccessful_add_raise_value_error_passenger_name_duplicity(self):
        self.train.capacity = 3
        self.train.add("Joro")
        self.train.add("Not Joro")

        with self.assertRaises(ValueError) as ve:
            self.train.add("Joro")

        self.assertEqual("Passenger Joro Exists", str(ve.exception))
        self.assertEqual(["Joro", "Not Joro"], self.train.passengers)

    def test_successful_add_passenger_return_string(self):
        self.train.add("Joro")
        result = self.train.add("Not Joro")

        self.assertEqual("Added passenger Not Joro", result)
        self.assertEqual(["Joro", "Not Joro"], self.train.passengers)

    def test_unsuccessful_remove_raise_value_error_passenger_name_not_in_list(self):
        self.train.add("Joro")
        self.train.add("Not Joro")

        with self.assertRaises(ValueError) as ve:
            self.train.remove("Georgi")

        self.assertEqual("Passenger Not Found", str(ve.exception))
        self.assertEqual(["Joro", "Not Joro"], self.train.passengers)

    def test_successful_remove_passenger_from_list_return_string(self):
        self.train.add("Joro")
        self.train.add("Not Joro")

        result = self.train.remove("Joro")
        self.assertEqual("Removed Joro", result)
        self.assertEqual(['Not Joro'], self.train.passengers)


if __name__ == "__main__":
    main()
