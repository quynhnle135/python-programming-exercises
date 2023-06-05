import unittest
from convert_int_to_str import convert_int_to_str


class TestConvertIntToStr(unittest.TestCase):
    def test_1(self):
        self.assertEqual(convert_int_to_str(42), str(42))

    def test_2(self):
        self.assertEqual(convert_int_to_str(15), str(15))

    def test_3(self):
        self.assertEqual(convert_int_to_str(-500), str(-500))

    def test_4(self):
        self.assertEqual(convert_int_to_str(-100), str(-100))

    def test_5(self):
        self.assertEqual(convert_int_to_str(0), str(0))

    def test_6(self):
        for i in range(-10000, 10000):
            self.assertEqual(convert_int_to_str(i), str(i))


if __name__ == "__main__":
    unittest.main()