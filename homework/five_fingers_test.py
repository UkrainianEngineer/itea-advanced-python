import unittest
from five_fingers_def import finger_name


class FiveFingersTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_five_fingers_n1_pinky(self):
        result = finger_name(1, ['pinky', 'ring', 'middle', 'index', 'thumb'])
        self.assertEqual(result, 'pinky')

    def test_five_fingers_n1_not_pinky(self):
        result = finger_name(1, ['pinky', 'ring', 'middle', 'index', 'thumb'])
        self.assertNotEqual(result, 'pinky')