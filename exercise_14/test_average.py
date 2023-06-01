import unittest
from average import find_average


class TestAverage(unittest.TestCase):
    def test_average_1(self):
        self.assertEqual(find_average([1, 2, 3]), 2)

    def test_average_2(self):
        self.assertEqual(find_average([1, 2, 3, 1, 2, 3, 1, 2, 3]), 2)

    def test_average_3(self):
        self.assertEqual(find_average([12, 20, 37]), 23)

    def test_average_4(self):
        self.assertEqual(find_average([0, 0, 0, 0]), 0)


if __name__ == "__main__":
    unittest.main()