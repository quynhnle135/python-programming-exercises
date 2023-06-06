from title_case import get_title_case
import unittest


class TestTitleCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_title_case("Hello, world!"), "Hello, World!")

    def test_2(self):
        self.assertEqual(get_title_case("HELLO"), "Hello")

    def test_3(self):
        self.assertEqual(get_title_case("hello"), "Hello")

    def test_4(self):
        self.assertEqual(get_title_case("hEllo"), "Hello")

    def test_5(self):
        self.assertEqual(get_title_case(""), "")

    def test_6(self):
        self.assertEqual(get_title_case("abc123xyz"), "Abc123Xyz")

    def test_7(self):
        self.assertEqual(get_title_case("cat dog rat"), "Cat Dog Rat")

    def test_8(self):
        self.assertEqual(get_title_case("cat,dog,rat"), "Cat,Dog,Rat")


if __name__ == "__main__":
    unittest.main()