from project.plantation import Plantation
from unittest import TestCase, main


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(9)

    def test_successful_initialization(self):
        self.assertEqual(9, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_unsuccessful_initialization_size_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            test = Plantation(-1)

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_unsuccessful_hire_worker_exists_raise_value_error(self):
        self.plantation.hire_worker("Joro")

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Joro")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_successful_hire_worker_append_to_list(self):
        result = self.plantation.hire_worker("Joro")

        self.assertEqual("Joro successfully hired.", result)
        self.assertTrue("Joro" in self.plantation.workers)

        result = self.plantation.hire_worker("Not Joro")

        self.assertEqual("Not Joro successfully hired.", result)
        self.assertTrue("Not Joro" in self.plantation.workers)

    def test__len__(self):
        test = Plantation(1)
        test.hire_worker("Joro")
        test.hire_worker("Not Joro")
        test.plants["Joro"] = ["Nuts"]
        test.plants["Not Joro"] = ["Not Nuts"]
        self.assertEqual(len(test), 2)

    def test_unsuccessful_planting_raise_value_error_worker_not_found(self):
        with self.assertRaises(ValueError) as va:
            self.plantation.planting("Joro", "Tomato")

        self.assertEqual("Worker with name Joro is not hired!", str(va.exception))

    def test_unsuccessful_planting_size_is_full_raise_value_error(self):
        self.plantation.plants = {"Joro": "Tommatooo"}
        self.plantation.workers = ["Joro"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Joro", "Nuts")
        self.assertEqual("The plantation is full!", str(ve.exception))
        self.assertTrue(len(self.plantation) + 4 >= 9)

    def test_successful_planting_worker_exists(self):
        self.plantation.hire_worker("Joro")
        self.plantation.planting("Joro", "my")
        result = self.plantation.planting("Joro", "Nuts")

        self.assertEqual("Joro planted Nuts.", result)
        self.assertEqual(2, len(self.plantation.plants["Joro"]))

    def test_successful_planting_worker_first_plant(self):
        self.plantation.workers = ["Joro", "not Joro"]
        result = self.plantation.planting("Joro", "Nuts")

        self.assertEqual("Joro planted it's first Nuts.", result)
        self.assertEqual({"Joro": ["Nuts"]}, self.plantation.plants)

        result = self.plantation.planting("not Joro", "Nuts")

        self.assertEqual("not Joro planted it's first Nuts.", result)
        self.assertEqual({"Joro": ["Nuts"], "not Joro": ["Nuts"]}, self.plantation.plants)

    def test__str__(self):

        self.assertEqual("Plantation size: 9\n", self.plantation.__str__())
        self.plantation.hire_worker("Joro")
        self.plantation.planting("Joro", "Nuts")
        self.assertEqual("Plantation size: 9\n"
                         "Joro\n"
                         "Joro planted: Nuts", self.plantation.__str__())

    def test__repr__(self):
        self.assertEqual("Size: 9\nWorkers: ", self.plantation.__repr__())
        self.plantation.hire_worker("Joro")
        self.plantation.planting("Joro", "Nuts")
        self.assertEqual("Size: 9\n"
                         "Workers: Joro", self.plantation.__repr__())


if __name__ == "__main__":
    main()
