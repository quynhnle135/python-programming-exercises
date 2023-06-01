import unittest
from median import find_median


class TestMedian(unittest.TestCase):
    def test_median_1(self):
        self.assertEqual(find_median([]), None)

    def test_median_2(self):
        self.assertEqual(find_median([1, 2, 3]), 2)

    def test_median_3(self):
        self.assertEqual(find_median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]), 5.5)

    def test_median_4(self):
        self.assertEqual(find_median([3, 7, 10, 4, 1, 9, 6, 2, 8]), 6)


if __name__ == "__main__":
    unittest.main()