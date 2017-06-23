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

if __name__ == '__main__':
    unittest.main()