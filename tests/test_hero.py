import unittest
from creatures.hero import Hero

class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Guerrier", 50, 15)

    def test_level_up(self):
        self.hero.gain_xp(100)
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.pv, 60)
        self.assertEqual(self.hero.defense, 17)

if __name__ == "__main__":
    unittest.main()
    