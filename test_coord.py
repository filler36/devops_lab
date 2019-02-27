import unittest
import coord


class TestCoord(unittest.TestCase):

    def setUp(self):
        """Init"""

    def test_result1(self):
        self.assertEqual(coord.calc(0, 0, 1, 1)[0], [0, 0, 0])

    def tearDown(self):
        """Finish"""
