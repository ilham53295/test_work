from program.alternation_characters import alternatingcharacter

import unittest

class TestAltCharacter(unittest.TestCase):
    def test_AAAAA_in_alt_characters(self):
        x = 'AAAAA'
        result = alternatingcharacter(x)
        self.assertEqual(result, 4)
    def test_BBBBBBB_in_alt_characters(self):
        x = 'BBBBBBB'
        result = alternatingcharacter(x)
        self.assertEqual(result, 6)
    def test_ABCDEFGHIJKLMNOPQRSTUVWXYZabc_in_alt_characters(self):
        x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabc'
        result = alternatingcharacter(x)
        self.assertEqual(result, 0)
    def test_AAAABBBB_in_alt_characters(self):
        x = 'AAAABBBB'
        result = alternatingcharacter(x)
        self.assertEqual(result, 6)
    def test_AABBCC_in_alt_characters(self):
        x = 'AABBCC'
        result = alternatingcharacter(x)
        self.assertEqual(result, 3)
