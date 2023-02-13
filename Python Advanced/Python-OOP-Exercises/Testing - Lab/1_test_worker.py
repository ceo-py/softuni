from unittest import TestCase, main


# from 1_christmas_pastry_shop.worker import Worker


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Test", 100, 100)

    def test_successful_initialization(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_successful_work(self):
        self.worker.work()
        self.assertEqual(100, self.worker.money)
        self.assertEqual(99, self.worker.energy)

    def test_unsuccessful_work_not_enough_energy_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_rest_adding_one_energy(self):
        self.worker.rest()

        self.assertEqual(101, self.worker.energy)

    def test_get_info_string_return(self):
        result = self.worker.get_info()

        self.assertEqual(f'Test has saved 0 money.', result)


if __name__ == "__main__":
    main()
