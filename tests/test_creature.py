import unittest
from creatures.creature import Creature

class TestCreature(unittest.TestCase):
    def setUp(self):
        self.creature = Creature("Gobelin", 30, 10)

    def test_is_alive(self):
        self.assertTrue(self.creature.is_alive())
        self.creature.pv = 0
        self.assertFalse(self.creature.is_alive())

    def test_take_damage(self):
        self.creature.take_damage(10)
        self.assertEqual(self.creature.pv, 20)
        self.creature.take_damage(30)
        self.assertEqual(self.creature.pv, 0)

if __name__ == "__main__":
    unittest.main()