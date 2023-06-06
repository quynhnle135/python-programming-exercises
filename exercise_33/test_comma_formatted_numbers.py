from comma_formatted_numbers import format_numbers
import unittest


class TestCommaFormattedNumber(unittest.TestCase):
    def test_1(self):
        self.assertEqual(format_numbers(1), '1')

    def test_2(self):
        self.assertEqual(format_numbers(10), '10')

    def test_3(self):
        self.assertEqual(format_numbers(100), '100')

    def test_4(self):
        self.assertEqual(format_numbers(1000), '1,000')

    def test_5(self):
        self.assertEqual(format_numbers(10000), '10,000')

    def test_6(self):
        self.assertEqual(format_numbers(100000), '100,000')

    def test_7(self):
        self.assertEqual(format_numbers(1000000), '1,000,000')


if __name__ == "__main__":
    unittest.main()