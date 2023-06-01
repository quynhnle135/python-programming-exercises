from mode import find_mode
import unittest


class TestMode(unittest.TestCase):
    def test_mode_1(self):
        self.assertEqual(find_mode([]), None)

    def test_mode_2(self):
        self.assertEqual(find_mode([1, 2, 3, 4, 4]), 4)

    def test_mode_3(self):
        self.assertEqual(find_mode([1, 1, 2, 3, 4]), 1)


if __name__ == "__main__":
    unittest.main()