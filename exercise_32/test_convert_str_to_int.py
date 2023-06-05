from convert_str_to_int import convert_str_to_int
import unittest


class TestConvertStrToInt(unittest.TestCase):
    def test(self):
        for i in range(-10000, 10000):
            self.assertEqual(convert_str_to_int(str(i)), i)


if __name__ == "__main__":
    unittest.main()