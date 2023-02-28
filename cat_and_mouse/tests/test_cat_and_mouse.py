from program.cat_and_mouse import cat_and_mouse

import unittest

class TestCatsMouse(unittest.TestCase):
    def test_1_2_3_in_CatMouse(self):
        result = cat_and_mouse(1,2,3)
        self.assertEqual(result, 'Cat B')
    def test_1_3_2_in_CatMouse(self):
        result = cat_and_mouse(1,3,2)
        self.assertEqual(result, 'Mouse C')
    def test_1_2_4_in_CatMouse(self):
        result = cat_and_mouse(1,2,4)
        self.assertEqual(result, 'Cat B')
    def test_3_3_3_in_CatMouse(self):
        result = cat_and_mouse(3,3,3)
        self.assertEqual(result, 'Mouse C')
    def test_8_3_4_in_CatMouse(self):
        result = cat_and_mouse(8,3,4)
        self.assertEqual(result, 'Cat B')