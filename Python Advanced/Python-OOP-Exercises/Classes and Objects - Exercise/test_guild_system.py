from project_guild.player import Player
from project_guild.guild import Guild

import unittest


class PlayerTest(unittest.TestCase):

    def test_player_init(self):
        player = Player("Pesho", 90, 90)
        result = player.player_info().strip()
        expected = "Name: Pesho\nGuild: Unaffiliated\nHP: 90\nMP: 90"
        self.assertEqual(result, expected)

    def test_adding_skill_should_work(self):
        player = Player("Pesho", 90, 90)
        message = player.add_skill("A", 3)
        expected = "Skill A added to the collection of the player Pesho"
        self.assertEqual(message, expected)

    # def test_adding_existing_skill_should_not_work(self):
    #     player = Player("Pesho", 90, 90)
    #     player.add_skill("A", 3)
    #     message = player.add_skill("A", 3)
    #     expected = "Skill already added"
    #     self.assertEqual(message, expected)

    def test_info(self):
        player = Player("Pesho", 90, 90)
        player.add_skill("A", 3)
        message = player.player_info().strip()
        expected = "Name: Pesho\nGuild: Unaffiliated\nHP: 90\nMP: 90\n===A - 3"
        self.assertEqual(message, expected)

    def test_guild_init(self):
        guild = Guild("GGXrd")
        message = guild.guild_info().strip()
        expeted = "Guild: GGXrd"
        self.assertEqual(message, expeted)

    def test_assign_working(self):
        guild = Guild("GGXrd")
        player = Player("Pesho", 90, 90)
        message = guild.assign_player(player)
        expected = "Welcome player Pesho to the guild GGXrd"
        self.assertEqual(message, expected)

    def test_assigning_player_in_the_same_guild(self):
        guild = Guild("GGXrd")
        player = Player("Pesho", 90, 90)
        guild.assign_player(player)
        message = guild.assign_player(player)
        expected = "Player Pesho is already in the guild."
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()
