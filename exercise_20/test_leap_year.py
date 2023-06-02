from leap_year import isLeapYear
import unittest


class TestLeapYear(unittest.TestCase):
    def test_1(self):
        self.assertEqual(isLeapYear(1999), False)

    def test_2(self):
        self.assertEqual(isLeapYear(2000), True)

    def test_3(self):
        self.assertEqual(isLeapYear(2001), False)

    def test_4(self):
        self.assertEqual(isLeapYear(2004), True)

    def test_5(self):
        self.assertEqual(isLeapYear(2100), False)

    def test_6(self):
        self.assertEqual(isLeapYear(2400), True)


if __name__ == "__main__":
    unittest.main()