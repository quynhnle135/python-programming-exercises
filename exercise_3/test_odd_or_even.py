import unittest
from odd_or_even import isOdd, isEven


class TestOddOrEven(unittest.TestCase):
    def test_is_odd_1(self):
        self.assertEqual(isOdd(12), False)

    def test_is_odd_2(self):
        self.assertEqual(isOdd(13), True)

    def test_is_odd_3(self):
        self.assertEqual(isOdd(1), True)

    def test_is_even_1(self):
        self.assertEqual(isEven(2), True)

    def test_is_even_2(self):
        self.assertEqual(isEven(3), False)

    def test_is_even_3(self):
        self.assertEqual(isEven(15), False)


if __name__ == "__main__":
    unittest.main()