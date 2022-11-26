from unittest import TestCase, main
from project.hero import Hero


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("RetroMan", 1, 20, 10)

    def test_successful_initialization(self):
        self.assertEqual("RetroMan", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(20, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_unsuccessful_battle_raise_exception_self_battle(self):
        with self.assertRaises(Exception) as ex:
            copy_ = Hero("RetroMan", 1, 20, 10)
            self.hero.battle(copy_)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_unsuccessful_battle_raise_value_error_hero_zero_or_negative_health(self):
        enemy_hero = Hero("ScrapMan", 1, 20, 10)
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_unsuccessful_battle_raise_value_error_enemy_zero_or_negative_health(self):
        enemy_hero = Hero("ScrapMan", 1, -1, 10)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight ScrapMan. He needs to rest", str(ve.exception))

    def test_successful_battle_draw(self):
        self.hero.damage = 20
        enemy_hero = Hero("ScrapMan", 1, 20, 20)
        result = self.hero.battle(enemy_hero)

        self.assertEqual("Draw", result)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, enemy_hero.health)

    def test_successful_battle_hero_win(self):
        enemy_hero = Hero("ScrapMan", 1, 20, 2)
        self.hero.damage = 20
        result = self.hero.battle(enemy_hero)
        self.assertEqual("You win", result)
        self.assertEqual(23, self.hero.health)
        self.assertEqual(0, enemy_hero.health)

    def test_successful_battle_hero_lose(self):
        enemy_hero = Hero("ScrapMan", 1, 20, 25)
        result = self.hero.battle(enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(-5, self.hero.health)
        self.assertEqual(15, enemy_hero.health)

    def test__str__(self):
        self.assertEqual("Hero RetroMan: 1 lvl\n"
                         "Health: 20\n"
                         "Damage: 10\n", str(self.hero))



if __name__ == "__main__":
    main()
