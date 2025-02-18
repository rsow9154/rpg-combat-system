import unittest
from ui.interface import Interface

class TestInterface(unittest.TestCase):
    def test_display_welcome(self):
        Interface.display_welcome()

if __name__ == "__main__":
    unittest.main()