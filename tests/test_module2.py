import unittest
from scripts.module2 import add

class Testmodule2(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)