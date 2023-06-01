import unittest
from smallest_and_biggest import find_biggest, find_smallest


class TestSmallestAndBiggest(unittest.TestCase):
    def test_get_smallest_1(self):
        self.assertEqual(find_smallest([1, 2, 3]), 1)

    def test_get_smallest_2(self):
        self.assertEqual(find_smallest([3, 2, 1]), 1)

    def test_get_smallest_3(self):
        self.assertEqual(find_smallest([-10, -15, -4, -99]), -99)

    def test_get_biggest_1(self):
        self.assertEqual(find_biggest([1, 2, 3, 4]), 4)

    def test_get_biggest_2(self):
        self.assertEqual(find_biggest([5, 4, 3, 2, 1]), 5)

    def test_get_biggest_3(self):
        self.assertEqual(find_biggest([28, 25, 42, 2, 28]), 42)


if __name__ == "__main__":
    unittest.main()