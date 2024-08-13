import unittest
from scripts.module1 import greet

class Testmodule1(unittest.TestCase):
    def test_module1(self):
        self.assertEqual(greet("getahun"),"Hello, getahun!")