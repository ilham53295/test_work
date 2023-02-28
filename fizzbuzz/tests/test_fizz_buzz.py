from program.fizz_buzz import fizz_buzz

import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_3_is_a_fizz(self):
        n = 3
        is_a_fizz_buzz = fizz_buzz(n)
        self.assertEqual(is_a_fizz_buzz, "Fizz")
    def test_15_is_a_fizz_buzz(self):
        n = 15
        is_a_fizz_buzz = fizz_buzz(n)
        self.assertEqual(is_a_fizz_buzz, "FizzBuzz")
    def test_5_is_a_buzz(self):
        n = 5
        is_a_buzz_buzz = fizz_buzz(n)
        self.assertEqual(is_a_buzz_buzz, "Buzz")
    def test_18_is_fizz(self):
        n = 18
        is_a_buzz_buzz = fizz_buzz(n)
        self.assertEqual(is_a_buzz_buzz, "Fizz")
    def test_30_is_fizz_Buzz(self):
        n = 30
        is_a_buzz_buzz = fizz_buzz(n)
        self.assertEqual(is_a_buzz_buzz, "FizzBuzz")