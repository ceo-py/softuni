from project.pokemon import Pokemon
from project.trainer import Trainer

import unittest


class PokemonTest(unittest.TestCase):
    def setUp(self):
        self.trainer = Trainer("Ash")
        self.pokemon = Pokemon("Pikachu", 90)
        self.second_pokemon = Pokemon("Charizard", 110)

    def test_pokemon_init(self):
        message = self.pokemon.pokemon_details()
        expected = "Pikachu with health 90"
        self.assertEqual(message, expected)

    def test_adding_pokemon(self):
        message = self.trainer.add_pokemon(self.pokemon)
        expected = "Caught Pikachu with health 90"
        self.assertEqual(message, expected)

    def test_adding_second_pokemon(self):
        message = self.trainer.add_pokemon(self.second_pokemon)
        expected = "Caught Charizard with health 110"
        self.assertEqual(message, expected)

    def test_adding_already_added_pokemon(self):
        self.trainer.add_pokemon(self.second_pokemon)
        message = self.trainer.add_pokemon(self.second_pokemon)
        expected = "This pokemon is already caught"
        self.assertEqual(message, expected)

    def test_releasing_pokemon(self):
        self.trainer.add_pokemon(self.pokemon)
        message = self.trainer.release_pokemon("Pikachu")
        expected = "You have released Pikachu"
        self.assertEqual(message, expected)

    def test_releasing_pokemon_that_is_not_caught(self):
        message = self.trainer.release_pokemon("Pikachu")
        expected = "Pokemon is not caught"
        self.assertEqual(message, expected)

    def test_trainer_data(self):
        self.trainer.add_pokemon(self.pokemon)
        self.trainer.add_pokemon(self.second_pokemon)
        self.trainer.release_pokemon("Pikachu")
        message = self.trainer.trainer_data()
        message = message.strip('\n')
        expected = "Pokemon Trainer Ash\nPokemon count 1\n- Charizard with health 110"
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()