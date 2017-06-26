import unittest
from five_fingers_def import finger_name


class FiveFingersTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_five_fingers_n1(self):
        result = finger_name(1, ['pinky', 'ring', 'middle', 'index', 'thumb'])
        self.assertEqual(result, 'pinky')

    def test_five_fingers_n2(self):
        result = finger_name(2, ['pinky', 'ring', 'middle', 'index', 'thumb'])
        self.assertEqual(result, 'ring')

    def test_five_fingers_n9(self):
        result = finger_name(9, ['pinky', 'ring', 'middle', 'index', 'thumb'])
        self.assertEqual(result, 'pinky')

    def test_five_fingers_n10(self):
        result = finger_name(10, ['pinky', 'ring', 'middle', 'index', 'thumb'])
        self.assertEqual(result, 'ring')

    def test_five_fingers_n1992(self):
        result = finger_name(1992, ['pinky', 'ring', 'middle', 'index', 'thumb'])
        self.assertEqual(result, 'ring')

    def test_four_fingers_n4(self):
        result = finger_name(4, ['pinky', 'ring', 'middle', 'index'])
        self.assertEqual(result, 'index')

    def test_four_fingers_n12(self):
        result = finger_name(12, ['pinky', 'ring', 'middle', 'index'])
        self.assertEqual(result, 'ring')

    def test_four_fingers_n8(self):
        result = finger_name(8, ['pinky', 'ring', 'middle', 'index'])
        self.assertEqual(result, 'ring')

    def test_four_fingers_n24(self):
        result = finger_name(24, ['pinky', 'ring', 'middle', 'index'])
        self.assertEqual(result, 'ring')

    def test_four_fingers_n6(self):
        result = finger_name(6, ['pinky', 'ring', 'middle', 'index'])
        self.assertEqual(result, 'ring')

    def test_four_fingers_n7(self):
        result = finger_name(7, ['pinky', 'ring', 'middle', 'index'])
        self.assertEqual(result, 'pinky')

    def test_three_fingers_n3(self):
        result = finger_name(3, ['pinky', 'ring', 'middle'])
        self.assertEqual(result, 'middle')

    def test_three_fingers_n5(self):
        result = finger_name(5, ['pinky', 'ring', 'middle'])
        self.assertEqual(result, 'pinky')

    def test_three_fingers_n10(self):
        result = finger_name(10, ['pinky', 'ring', 'middle'])
        self.assertEqual(result, 'ring')

    def test_six_fingers_n7(self):
        result = finger_name(7, ['minipinky', 'pinky', 'ring', 'middle', 'index', 'thumb'])
        self.assertEqual(result, 'index')

    def test_seven_fingers_n7(self):
        result = finger_name(7, ['minipinky', 'pinky', 'ring', 'middle', 'index', 'thumb', 'megathumb'])
        self.assertEqual(result, 'megathumb')

    def test_seven_fingers_n30(self):
        result = finger_name(30, ['minipinky', 'pinky', 'ring', 'middle', 'index', 'thumb', 'megathumb'])
        self.assertEqual(result, 'thumb')

if __name__ == '__main__':
    unittest.main()