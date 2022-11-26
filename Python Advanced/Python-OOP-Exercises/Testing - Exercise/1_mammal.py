from unittest import TestCase, main
from project.mammal import Mammal


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Dino", "BIG", "BRRRRRRrrr")

    def test_successful_init(self):
        self.assertEqual("Dino", self.mammal.name)
        self.assertEqual("BIG", self.mammal.type)
        self.assertEqual("BRRRRRRrrr", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_successful_make_sound_str(self):
        result = self.mammal.make_sound()
        self.assertEqual("Dino makes BRRRRRRrrr", result)

    def test_successful_get_kingdom_str(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_successful_info_str(self):
        result = self.mammal.info()
        self.assertEqual("Dino is of type BIG", result)

if __name__ == "__main__":
    main()
