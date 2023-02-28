from coe_number.number_utils import is_prime_list

import unittest
class PrimeListTest(unittest.TestCase):
    def test_give_2_3_is_prime(self):
        prime_list = [2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_4_5_6_is_not_prime(self):
        prime_list = [4,5,6]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
    def test_give_n1_0_1_is_Not_prime(self):
        prime_list = [-1,0,1]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
    def test_give_4_10_is_Not_prime(self):
        prime_list = range(4,11)
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
    def test_give_13_17_23_is_prime(self):
        prime_list = [13,17,23]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)