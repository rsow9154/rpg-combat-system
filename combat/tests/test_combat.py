import unittest
from creatures.hero import Hero
from creatures.monster import Monster
from combat.combat_manager import CombatManager

class TestCombat(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Guerrier", 50, 15)
        self.monster = Monster("Gobelin", 30, 10)
        self.combat_manager = CombatManager([self.hero, self.monster])

    def test_combat_turns(self):
        self.assertEqual(self.combat_manager.get_current_creature(), self.hero)
        self.combat_manager.next_turn()
        self.assertEqual(self.combat_manager.get_current_creature(), self.monster)

if __name__ == "__main__":
    unittest.main()