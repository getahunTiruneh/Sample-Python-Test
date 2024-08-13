import unittest
from scripts.module2 import add

class Testmodule2(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        expected = 5
        self.assertEqual(result,expected)