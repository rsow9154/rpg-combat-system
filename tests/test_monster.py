import unittest
from creatures.monster import Monster

class TestMonster(unittest.TestCase):
    def setUp(self):
        self.monster = Monster("Gobelin", 30, 10)

    def test_is_resistant(self):
        self.monster.resistances = ["feu"]
        self.assertTrue(self.monster.is_resistant("feu"))
        self.assertFalse(self.monster.is_resistant("tranchant"))

if __name__ == "__main__":
    unittest.main()