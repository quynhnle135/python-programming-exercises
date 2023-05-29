import unittest
from odd_or_even import isOdd, isEven


class TestOddOrEven(unittest.TestCase):
    def test_is_odd_1(self):
        self.assertEqual(isOdd(12), False)

    def test_is_odd_2(self):
        self.assertEqual(isOdd(13), True)

    def test_is_odd_3(self):
        self.assertEqual(isOdd(1), True)

    def test_is_odd_4(self):
        self.assertEqual(isOdd(9999), True)

    def test_is_odd_5(self):
        self.assertEqual(isOdd(42), False)

    def test_is_odd_6(self):
        self.assertEqual(isOdd(-10), False)

    def test_is_odd_7(self):
        self.assertEqual(isOdd(-11), True)

    def test_is_odd_8(self):
        self.assertEqual(isOdd(3.1415), False)

    def test_is_even_1(self):
        self.assertEqual(isEven(2), True)

    def test_is_even_2(self):
        self.assertEqual(isEven(3), False)

    def test_is_even_3(self):
        self.assertEqual(isEven(15), False)

    def test_is_even_4(self):
        self.assertEqual(isEven(9999), False)

    def test_is_even_5(self):
        self.assertEqual(isEven(-10), True)

    def test_is_even_6(self):
        self.assertEqual(isEven(-11), False)

    def test_is_even_7(self):
        self.assertEqual(isEven(3.1415), False)


if __name__ == "__main__":
    unittest.main()