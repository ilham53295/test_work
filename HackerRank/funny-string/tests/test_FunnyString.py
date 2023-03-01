from program.FunnyString import funnyString

import unittest

class TestFunnyString(unittest.TestCase):
    def test_acxz_in_FunnyString(self):
        x = 'acxz'
        result = funnyString(x)
        self.assertEqual(result, 'Funny')
    def test_abcd_in_FunnyString(self):
        x = 'abcd'
        result = funnyString(x)
        self.assertEqual(result, 'Funny')
    def test_2_in_FunnyString(self):
        x = '2'
        result = funnyString(x)
        self.assertEqual(result, 'Funny')
    def test_bvxz_in_FunnyString(self):
        x = 'bvxz'
        result = funnyString(x)
        self.assertEqual(result, 'Not Funny')
    def test_nbvc_in_FunnyString(self):
        x = 'nbvc'
        result = funnyString(x)
        self.assertEqual(result, 'Not Funny')