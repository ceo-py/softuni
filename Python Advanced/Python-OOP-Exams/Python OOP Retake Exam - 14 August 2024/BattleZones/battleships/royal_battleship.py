from project.battleships.base_battleship import BaseBattleship

class RoyalBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 100
    AMMUNITION_PER_ATTACK = 25

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, ammunition=self.INITIAL_AMMUNITION)

    def attack(self):
        # self.ammunition = max(0, self.ammunition - self.AMMUNITION_PER_ATTACK)

        self.ammunition -= self.AMMUNITION_PER_ATTACK
        if self.ammunition < 0:
            self.ammunition = 0
