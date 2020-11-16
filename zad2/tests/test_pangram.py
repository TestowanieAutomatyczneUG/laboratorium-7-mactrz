import unittest
from parameterized import parameterized, parameterized_class
from src.sample.pangram import *

class PangramTest(unittest.TestCase):

    def setUp(self):
        self.tmp = Pangram()
    @parameterized.expand([
        ('all', 'abcdefghijklmnopqrstuvwxyz', True),
        ('notall', 'abcdefghijklmnopqrstuyz', False),
        ('withnum', 'abcdefghijklmn341opqrstuvwxyz', True),
        ('onlynum', '1234', False),
        ('repeat', 'abcdefghijklmzzznopqwrstuaavawxyz', True)
    ])
    def test(self, name, val, expected):
        self.assertEqual(self.tmp.check(val), expected)

    @parameterized.expand([
        ('int', 23),
        ('boolean', True)
    ])
    def test_exception(self, name, text):
        with self.assertRaises(Exception):
            self.tmp.check(text)

    def tearDown(self):
        self.temp = None