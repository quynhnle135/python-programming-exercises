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

    def test_6(self):
        self.assertEqual(validate_date(1999, 12, 31), True)

    def test_7(self):
        self.assertEqual(validate_date(2000, 2, 29), True)

    def test_8(self):
        self.assertEqual(validate_date(2001, 2, 29), False)

    def test_10(self):
        self.assertEqual(validate_date(2029, 13, 1), False)

    def test_11(self):
        self.assertEqual(validate_date(1000000, 1, 1), True)

    def test_12(self):
        self.assertEqual(validate_date(2015, 4, 31), False)

    def test_13(self):
        self.assertEqual(validate_date(1970, 5, 99), False)

    def test_14(self):
        self.assertEqual(validate_date(1981, 0, 3), False)

    def test_15(self):
        self.assertEqual(validate_date(1666, 4, 0), False)


if __name__ == "__main__":
    unittest.main()