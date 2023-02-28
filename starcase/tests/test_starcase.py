from program import starcase

import unittest

class TestStarcase(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        n = 2
        pattern = '#'
        expected_output = \
        " #\n" + "##"

        result = starcase.starcase(n)
        self.assertEqual(result, expected_output, f'should be {expected_output}')
    def test_give_5_with_hash_should_be_hh(self):
        n = 5
        pattern = '#'
        expected_output = \
        "    #\n" + "   ##\n" + "  ###\n" + " ####\n" + "#####" 

        result = starcase.starcase(n)
        self.assertEqual(result, expected_output, f'should be {expected_output}')