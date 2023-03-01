from program.grid_challenge import gridchallenge

import unittest

class TestGridChallenge(unittest.TestCase):
    def test_give_exampleList_1_to_grid(self):
        lst = ['eabcd','fghij','olkmn','trpqs','xywuv']
        expected_output = 'YES'
        result = gridchallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')

    def test_give_exampleList_2_to_grid(self):
        lst = ['mpxz','abcd','wlmf']
        expected_output = 'NO'
        result = gridchallenge(lst)
        self.assertEqual(result, expected_output , f'Shoud be {expected_output}')

    def test_give_exampleList_3_to_grid(self):
        lst = ['zzzzzwz','zzzzzzw','wzzzzzz','zzwzzzz','zzyzzzz','zzzzyzz','zzzzzyz']
        expected_output = 'YES'
        result = gridchallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')

    def test_give_exampleList_4_to_grid(self):
        lst = ['rpb','hot','qra']
        expected_output = 'NO'
        result = gridchallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')
    def test_give_exampleList_5_to_grid(self):
        lst = ['Hello', 'around', 'worl', 'we', 'okey']
        excepted_output = 'NO'
        result = gridchallenge(lst)
        self.assertEqual(result, excepted_output, f'Shoud be {excepted_output}')