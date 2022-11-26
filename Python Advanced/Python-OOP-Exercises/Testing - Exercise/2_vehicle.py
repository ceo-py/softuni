from unittest import TestCase, main
from project.vehicle import Vehicle


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(56, 51)

    def test_successful_initialization(self):
        self.assertEqual(56, self.vehicle.fuel)
        self.assertEqual(56, self.vehicle.capacity)
        self.assertEqual(51, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_unsuccessful_drive_raise_exception(self):
        kilometers = 1000
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(kilometers)

        self.assertTrue(kilometers * 1.25 > self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_successful_drive(self):
        kilometers = 10
        self.vehicle.drive(kilometers)
        self.assertTrue(kilometers * 1.25 <= self.vehicle.fuel)
        self.assertEqual(43.5, self.vehicle.fuel)

    def test_unsuccessful_refuel_raise_exception(self):
        fuel = 1000
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(fuel)

        self.assertTrue(fuel + self.vehicle.fuel > self.vehicle.capacity)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_successful_refuel(self):
        self.vehicle.capacity = 66
        fuel = 10
        self.assertTrue(fuel + self.vehicle.fuel <= self.vehicle.capacity)
        self.vehicle.refuel(fuel)
        self.assertEqual(66, self.vehicle.fuel)

    def test___str__(self):
        result = str(self.vehicle)
        self.assertEqual("The vehicle has 51 horse power "
                         "with 56 fuel left and "
                         "1.25 fuel consumption", result)


if __name__ == "__main__":
    main()
