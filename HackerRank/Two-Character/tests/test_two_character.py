from program.two_character import twocharacter

import unittest

class TestTwoCharacter(unittest.TestCase):
    def test_give_ILoveYou_to_Two_Character(self):
        text = 'ILoveYou'
        excepted_output = 3
        result = twocharacter(text)
        self.assertEqual(result, excepted_output, f'Should be {excepted_output}')
    def test_give_zxcvbnmlkhgfd_to_two_character(self):
        text = 'zxcvbnmlkhgfd'
        excepted_output = 2
        result = twocharacter(text)
        self.assertEqual(result, excepted_output, f'Should be {excepted_output}')
    def test_give_asgxcugdsugcewuigcvkejwvcyewbcekwjcgv_to_two_character(self):
        text = 'asgxcugdsugcewuigcvkejwvcyewbcekwjcgv'
        excepted_output = 8
        result = twocharacter(text)
        self.assertEqual(result, excepted_output, f'Should be {excepted_output}')
    def test_give_ac_to_two_character(self):
        text = 'ac'
        excepted_output = 2
        result = twocharacter(text)
        self.assertEqual(result, excepted_output, f'Should be {excepted_output}')
    def test_give_Hello_World_two_character(self):
        text = 'Hello world'
        excepted_output = 3
        result = twocharacter(text)
        self.assertEqual(result, excepted_output, f'Should be {excepted_output}')