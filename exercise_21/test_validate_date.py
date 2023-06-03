from validate_date import validate_date
import unittest

class TestValidateDate(unittest.TestCase):
    def test_1(self):
        self.assertEqual(validate_date(2020, 2, 29), True)

    def test_2(self):
        self.assertEqual(validate_date(2020, 2, 30), False)

    def test_3(self):
        self.assertEqual(validate_date(2023, 5, 13), True)

    def test_4(self):
        self.assertEqual(validate_date(2023, 5, 32), False)

    def test_5(self):
        self.assertEqual(validate_date(2023, 5, 0), False)


if __name__ == "__main__":
    unittest.main()