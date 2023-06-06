from merge_two_sorted_lists import merge
import unittest


class TestMergeTwoSortedLists(unittest.TestCase):
    def test_1(self):
        self.assertEqual(merge([1, 3, 6], [5, 7, 8, 9]), [1, 3, 5, 6, 7, 8, 9])

    def test_2(self):
        self.assertEqual(merge([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5])

    def test_3(self):
        self.assertEqual(merge([2, 2, 2], [2, 2, 2]), [2, 2, 2, 2, 2, 2])

    def test_4(self):
        self.assertEqual(merge([], [1, 2, 3]), [1, 2, 3])

    def test_5(self):
        self.assertEqual(merge([1, 2, 3], []), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()